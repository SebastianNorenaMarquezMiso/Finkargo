from flask import request, jsonify
from domain.services.rol_service import RolService


class RolController:
    def __init__(self, db):
        self.rol_service = RolService(db)

    def add_rol(self):
        data = request.json
        nombre = data['nombre']
        rol_id = self.rol_service.add_rol(nombre)
        return jsonify({'message': 'Rol agregado correctamente', 'id': rol_id})

    def get_rol(self, id):
        rol = self.rol_service.get_rol(id)
        if rol:
            return jsonify({'rol': rol.__dict__})
        else:
            return jsonify({'message': 'Rol no encontrado'})

    def update_rol(self, id):
        data = request.json
        nombre = data['nombre']
        self.rol_service.update_rol(id, nombre)
        return jsonify({'message': 'Rol actualizado correctamente'})

    def delete_rol(self, id):
        self.rol_service.delete_rol(id)
        return jsonify({'message': 'Rol eliminado correctamente'})
