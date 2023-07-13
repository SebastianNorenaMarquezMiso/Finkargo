from infrastructure.persistence.database import Database
from .rol_repository import RolRepository
from domain.models.usuario import Usuario
from sqlalchemy import text


class UsuarioRepository:
    def __init__(self, db: Database):
        self.db = db

    def add_usuario(self, usuario):
        # Verificar si el rol existe
        rol = RolRepository(self.db).rol_exists(usuario.rol_id)
        if not rol:
            raise ValueError("El rol especificado no existe")

        self.db.execute(
            str(text("INSERT INTO Usuarios (nombre, correo, rol_id) VALUES (:nombre, :correo, :rol_id)")),
            [{"nombre": usuario.nombre, "correo": usuario.correo, "rol_id": usuario.rol_id}]
        )

    def get_usuario(self, id):
        # Consulta SQL para obtener los datos del usuario con un ID específico
        query = str(text("SELECT * FROM Usuarios WHERE id = :id_user"))

        # Parámetros de la consulta
        params = {"id_user": id}

        # Ejecutar la consulta y obtener el resultado
        result = self.db.fetch_one(query, params)

        # Comprobar si se encontró un resultado
        if result is not None:
            # Crear un objeto Usuario a partir de los datos
            usuario = Usuario(
                id=result.id,
                nombre=result.nombre,
                correo=result.correo,
                rol_id=result.rol_id
            )
            return usuario

        # Si no se encontró ningún usuario, devolver None
        return None

    def update_usuario(self, id, patch_data):
        usuario = self.get_usuario(id)
        if not usuario:
            return None

        # Aplicar las modificaciones del patch al objeto usuario
        for key, value in patch_data.items():
            setattr(usuario, key, value)

        # Utilizar merge para actualizar el objeto en la sesión
        updated_usuario = self.db.session.merge(usuario)
        self.db.session.commit()
        return updated_usuario

    def delete_usuario(self, id):
        if not self.usuario_exists(id):
            raise ValueError("El usuario especificado no existe")
        self.db.execute(
            str(text("DELETE FROM Usuarios WHERE id = :id_user")),
            [{"id_user": id}]
        )

    def usuario_exists(self, id):
        result = self.db.execute(
            str(text("SELECT COUNT(*) FROM Usuarios WHERE id = :id_user")),
            [{"id_user": id}]
        ).scalar()
        return result > 0
