

class MatrizController:
    def __init__(self, matriz_service):
        self.matriz_service = matriz_service

    def ordenar_matriz(self, data):
        matriz = data['sin clasificar']
        matriz_clasificada = self.matriz_service.ordenar_matriz(matriz)
        return {
            'clasificado': matriz_clasificada,
            'sin clasificar': matriz,
        }
