import unittest
from flask import Flask, jsonify
from flask_testing import TestCase

from adapters.controllers.balance_controller import BalanceController


class BalanceControllerTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        return app

    def setUp(self):
        self.controller = BalanceController()

    def test_calcular_balance(self):
        # Datos de ejemplo
        data = {
            'Mes': ['Enero', 'Febrero', 'Marzo'],
            'Ventas': [1000, 2000, 1500],
            'Gastos': [500, 1000, 800]
        }

        # Resultado esperado
        expected_result = jsonify([
            {'Mes': 'Enero', 'Ventas': 1000, 'Gastos': 500, 'Balance': 500},
            {'Mes': 'Febrero', 'Ventas': 2000, 'Gastos': 1000, 'Balance': 1000},
            {'Mes': 'Marzo', 'Ventas': 1500, 'Gastos': 800, 'Balance': 700}
        ])

        # Llamar al método calcular_balance
        result = self.controller.calcular_balance(data)

        # Verificar si el resultado es el esperado
        self.assertEqual(result.data, expected_result.data)


if __name__ == '__main__':
    unittest.main()
