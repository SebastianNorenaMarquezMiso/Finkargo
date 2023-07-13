from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rol(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    usuarios = relationship('Usuario', backref='rol')
    permisos = relationship('Permiso', backref='rol')

    def __repr__(self):
        return f'<Rol {self.nombre}>'


class Permiso(Base):
    __tablename__ = 'Permisos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    rol_id = Column(Integer, ForeignKey('Roles.id'), nullable=False)

    def __repr__(self):
        return f'<Permiso {self.nombre}>'


class Usuario(Base):
    __tablename__ = 'Usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(100), nullable=False)
    rol_id = Column(Integer, ForeignKey('Roles.id'), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'rol_id': self.rol_id
        }
