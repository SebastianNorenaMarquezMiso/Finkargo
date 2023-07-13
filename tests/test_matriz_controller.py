import unittest
from unittest.mock import MagicMock

from adapters.controllers.matriz_controller import MatrizController


class MatrizControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.matriz_service_mock = MagicMock()
        self.controller = MatrizController(self.matriz_service_mock)

    def test_ordenar_matriz(self):
        # Datos de ejemplo
        data = {
            'sin clasificar': [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        }

        # Matriz clasificada esperada
        matriz_clasificada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Configurar el mock del servicio de matriz
        self.matriz_service_mock.ordenar_matriz.return_value = matriz_clasificada

        # Resultado esperado
        expected_result = {
            'clasificado': matriz_clasificada,
            'sin clasificar': data['sin clasificar']
        }
        # Llamar al método ordenar_matriz
        result = self.controller.ordenar_matriz(data)
        # Verificar si el resultado es el esperado
        self.assertEqual(result, expected_result)
        self.matriz_service_mock.ordenar_matriz.assert_called_once_with(data['sin clasificar'])


if __name__ == '__main__':
    unittest.main()
