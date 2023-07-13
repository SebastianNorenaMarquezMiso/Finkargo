from domain.models.usuario import Usuario
from adapters.repositories.usuario_repository import UsuarioRepository
from adapters.repositories.rol_repository import RolRepository


class UsuarioService:
    def __init__(self, db):
        self.usuario_repository = UsuarioRepository(db)
        self.rol_repository = RolRepository(db)

    def rol_exists(self, rol_id):
        rol = self.rol_repository.get_rol(rol_id)
        return rol is not None

    def add_usuario(self, nombre, correo, rol_id):
        usuario = Usuario(id=None, nombre=nombre, correo=correo, rol_id=rol_id)
        self.usuario_repository.add_usuario(usuario)

    def get_usuario(self, id):
        return self.usuario_repository.get_usuario(id)

    def update_usuario(self, usuario_id, nombre, correo, rol_id):
        # Verificar si el usuario existe
        usuario = self.usuario_repository.get_usuario(usuario_id)
        if not usuario:
            return None

        # Crear un diccionario con los datos actualizados
        patch_data = {
            'nombre': nombre,
            'correo': correo,
            'rol_id': rol_id
        }

        # Actualizar el usuario utilizando el repositorio
        self.usuario_repository.update_usuario(usuario_id, patch_data)
        return usuario

    def delete_usuario(self, id):
        self.usuario_repository.delete_usuario(id)
