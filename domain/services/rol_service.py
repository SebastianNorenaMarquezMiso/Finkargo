from domain.models.usuario import Rol
from adapters.repositories.rol_repository import RolRepository


class RolService:
    def __init__(self, db):
        self.rol_repository = RolRepository(db)

    def add_rol(self, nombre):
        rol = Rol(id=None, nombre=nombre)
        self.rol_repository.add_rol(rol)

    def get_rol(self, id):
        return self.rol_repository.get_rol(id)

    def update_rol(self, id, nombre):
        rol = self.rol_repository.get_rol(id)
        if rol:
            rol.nombre = nombre
            self.rol_repository.update_rol(rol)

    def delete_rol(self, id):
        self.rol_repository.delete_rol(id)

    def get_roles(self):
        return self.rol_repository.get_roles()
