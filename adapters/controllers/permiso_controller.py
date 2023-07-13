from flask import request, jsonify
from domain.services.permiso_service import PermisoService


class PermisoController:
    def __init__(self, db):
        self.permiso_service = PermisoService(db)

    def add_permiso(self):
        data = request.json
        nombre = data['nombre']
        permiso_id = self.permiso_service.add_permiso(nombre)
        return jsonify({'message': 'Permiso agregado correctamente', 'id': permiso_id})

    def get_permiso(self, id):
        permiso = self.permiso_service.get_permiso(id)
        if permiso:
            return jsonify({'permiso': permiso.__dict__})
        else:
            return jsonify({'message': 'Permiso no encontrado'})

    def update_permiso(self, id):
        data = request.json
        nombre = data['nombre']
        self.permiso_service.update_permiso(id, nombre)
        return jsonify({'message': 'Permiso actualizado correctamente'})

    def delete_permiso(self, id):
        self.permiso_service.delete_permiso(id)
        return jsonify({'message': 'Permiso eliminado correctamente'})
