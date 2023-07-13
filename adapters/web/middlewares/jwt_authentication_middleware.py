# adapters/web/middlewares/jwt_authentication_middleware.py
from flask import request, abort
import jwt


class JWTAuthenticationMiddleware:
    @staticmethod
    def validate():
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            abort(401)

        token = auth_header.split(' ')[1]
        try:
            jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
        except jwt.InvalidTokenError:
            abort(401)
