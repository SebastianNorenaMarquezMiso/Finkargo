# adapters/controllers/auth_controller.py
import jwt


class AuthController:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generar_token(self, usuario, password):
        payload = {
            'usuario': usuario,
            'password': password,
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return {'token': token}
