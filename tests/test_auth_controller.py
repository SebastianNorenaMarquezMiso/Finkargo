import unittest
from unittest.mock import MagicMock
import jwt

from adapters.controllers.auth_controller import AuthController


class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.secret_key = 'secret'
        self.auth_controller = AuthController(self.secret_key)

    def test_generar_token(self):
        usuario = 'usuario1'
        password = 'password1'
        expected_token = 'example_token'

        jwt.encode = MagicMock(return_value=expected_token)

        result = self.auth_controller.generar_token(usuario, password)

        jwt.encode.assert_called_once_with(
            {'usuario': usuario, 'password': password},
            self.secret_key,
            algorithm='HS256'
        )
        self.assertEqual(result, {'token': expected_token})


if __name__ == '__main__':
    unittest.main()
