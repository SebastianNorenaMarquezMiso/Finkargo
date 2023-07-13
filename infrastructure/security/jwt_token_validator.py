import jwt


class JWTTokenValidator:
    @staticmethod
    def validate(token):
        # Implementación para validar el token JWT
        try:
            # decoded_token = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
            # TODO:validacion de  token
            return True
        except jwt.InvalidTokenError:
            return False
