import numpy as np


def is_symmetric(matrix):
    # Converte a lista de listas para um array NumPy
    mat = np.array(matrix)

    # Verifica se a matriz é igual à sua transposta
    return np.array_equal(mat, mat.T)


# Exemplo de uso
matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matriz):
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")