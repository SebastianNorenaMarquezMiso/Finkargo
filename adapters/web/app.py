from flask import Flask, request, jsonify
from adapters.controllers.matriz_controller import MatrizController
from adapters.controllers.auth_controller import AuthController
from adapters.controllers.balance_controller import BalanceController
from domain.services.matriz_service import MatrizService
from adapters.web.middlewares.input_validation_middleware import InputValidationMiddleware
from adapters.web.middlewares.jwt_authentication_middleware import JWTAuthenticationMiddleware
from adapters.controllers.usuario_controller import UsuarioController
from adapters.controllers.rol_controller import RolController
from adapters.controllers.permiso_controller import PermisoController
from infrastructure.config.schemas import MATRIZ_SCHEMA, TOKEN_REQUEST_SCHEMA, BALANCE_SCHEMA, USER_SHEMA
from infrastructure.persistence.database import Database

app = Flask(__name__)

# Configurar la conexión a la base de datos
database = Database.get_instance()
service = MatrizService()
auth_controller = AuthController('SECRET_KEY')
controller = MatrizController(service)
balance_controller = BalanceController()
usuario_controller = UsuarioController(database)
RolController(database)
PermisoController(database)


@app.before_request
def before_request():
    # Verificar autorización solo para endpoints diferentes a /token
    if request.path != '/token':
        JWTAuthenticationMiddleware.validate()


@app.route('/token', methods=['POST'])
def generar_token():
    data = request.json
    InputValidationMiddleware.validate(data, TOKEN_REQUEST_SCHEMA)
    usuario = data['usuario']
    password = data['password']
    response = auth_controller.generar_token(usuario, password)
    return jsonify(response)


@app.route('/ordenar', methods=['POST'])
def ordenar_matriz():
    data = request.json
    InputValidationMiddleware.validate(data, MATRIZ_SCHEMA)
    response = controller.ordenar_matriz(data)
    return jsonify(response)


@app.route('/balance', methods=['POST'])
def calcular_balance():
    data = request.json
    InputValidationMiddleware.validate(data, BALANCE_SCHEMA)
    response = balance_controller.calcular_balance(data)
    return jsonify(response.json)


@app.route('/usuarios', methods=['POST'])
def add_usuario():
    data = request.json
    InputValidationMiddleware.validate(data, USER_SHEMA)
    return usuario_controller.add_usuario()


@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    return usuario_controller.get_usuario(id)


@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.json
    InputValidationMiddleware.validate(data, USER_SHEMA)
    return usuario_controller.update_usuario(id)


@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        return usuario_controller.delete_usuario(id), 200
    except ValueError as e:
        return str(e), 404


if __name__ == '__main__':
    app.run()
