from flask import request, jsonify
from domain.services.usuario_service import UsuarioService


class UsuarioController:
    def __init__(self, db):
        self.usuario_service = UsuarioService(db)

    def add_usuario(self):
        data = request.json
        nombre = data['nombre']
        correo = data['correo']
        rol_id = data['rol_id']
        # Verificar si el rol existe
        if not self.usuario_service.rol_exists(rol_id):
            return jsonify({'message': 'El rol especificado no existe'})

        self.usuario_service.add_usuario(nombre, correo, rol_id)
        return jsonify({'message': 'Usuario agregado correctamente'})

    def get_usuario(self, id):
        usuario = self.usuario_service.get_usuario(id)
        if usuario:
            return jsonify({'usuario': usuario.to_dict()})
        else:
            return jsonify({'message': 'Usuario no encontrado'})

    def update_usuario(self, id):
        data = request.json
        nombre = data['nombre']
        correo = data['correo']
        rol_id = data['rol_id']
        usuario = self.usuario_service.update_usuario(id, nombre, correo, rol_id)
        if not usuario:
            return jsonify({'mensaje': 'El usuario especificado no existe'})
        return jsonify({'message': 'Usuario actualizado correctamente'})

    def delete_usuario(self, id):
        self.usuario_service.delete_usuario(id)
        return jsonify({'message': 'Usuario eliminado correctamente'})
