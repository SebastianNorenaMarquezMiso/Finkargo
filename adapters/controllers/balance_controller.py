from flask import jsonify


class BalanceController:
    def calcular_balance(self, data):
        # Obtener los datos del diccionario
        meses = data['Mes']
        ventas = data['Ventas']
        gastos = data['Gastos']

        # Calcular el balance para cada mes utilizando funciones flecha
        balances = list(map(lambda venta, gasto: venta - gasto, ventas, gastos))

        # Crear la respuesta JSON con la información y el balance utilizando funciones flecha
        respuesta = list(map(lambda mes, venta, gasto, balance: {
            'Mes': mes,
            'Ventas': venta,
            'Gastos': gasto,
            'Balance': balance
        }, meses, ventas, gastos, balances))
        return jsonify(respuesta)
