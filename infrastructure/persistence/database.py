from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from domain.models.usuario import Rol, Permiso, Usuario
Base = declarative_base()


class Database:
    _instance = None

    @staticmethod
    def get_instance():
        if not Database._instance:
            Database._instance = Database()
        return Database._instance

    def __init__(self):
        if Database._instance:
            raise Exception("Database instance already exists. Use get_instance() to retrieve it.")
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self._instance = self

        # Crear las tablas en la base de datos
        self.create_tables()

        # Insertar valores por defecto en la tabla Rol y Permiso
        self.insert_default_data()

    def create_tables(self):
        Base.metadata.create_all(bind=self.session.get_bind(), tables=[Rol.__table__, Usuario.__table__, Permiso.__table__])

    def insert_default_data(self):
        # Verificar si ya existen registros en la tabla Rol
        existing_roles = self.session.query(Rol).count()

        # Si no existen registros, insertar valores por defecto
        if existing_roles == 0:
            rol_defecto = Rol(nombre='Rol por Defecto')
            self.session.add(rol_defecto)
            self.session.commit()

            permiso_defecto = Permiso(nombre='Permiso por Defecto', rol_id=rol_defecto.id)
            self.session.add(permiso_defecto)
            self.session.commit()

    def execute(self, query, params=None):
        result = self.session.execute(text(query), params if params is not None else [])
        self.session.commit()
        return result

    def fetch_all(self, query, params=None):
        result = self.session.execute(query, params)
        return result.fetchall()

    def fetch_one(self, query, params=None):
        if params is None:
            params = {}
        result = self.session.execute(text(query), params)
        return result.fetchone()

    def close(self):
        self.session.close()
