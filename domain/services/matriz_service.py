class MatrizService:

    def ordenar_matriz(self, matriz):
        duplicados = filter(lambda x: matriz.count(x) > 1, matriz)
        matriz_ordenada = sorted(set(matriz))
        matriz_ordenada.extend(set(duplicados))
        return matriz_ordenada
