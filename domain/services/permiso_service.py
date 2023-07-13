from domain.models.usuario import Permiso
from adapters.repositories.permiso_repository import PermisoRepository


class PermisoService:
    def __init__(self, db):
        self.permiso_repository = PermisoRepository(db)

    def add_permiso(self, nombre):
        permiso = Permiso(id=None, nombre=nombre)
        self.permiso_repository.add_permiso(permiso)

    def get_permiso(self, id):
        return self.permiso_repository.get_permiso(id)

    def update_permiso(self, id, nombre):
        permiso = self.permiso_repository.get_permiso(id)
        if permiso:
            permiso.nombre = nombre
            self.permiso_repository.update_permiso(permiso)

    def delete_permiso(self, id):
        self.permiso_repository.delete_permiso(id)

    def get_permisos(self):
        return self.permiso_repository.get_permisos()
