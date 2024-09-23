import numpy as np

# Definindo a matriz A e a matriz B
A = np.array([[2, 0, 0],
              [6, 1, 0],
              [-8, 5, 3]])

B = np.array([[1],
              [2],
              [3]])

# Resolvendo o sistema de equações
X = np.linalg.solve(A, B)

# Extraindo os valores de x, y e z
x, y, z = X.flatten()  # flatten transforma a matriz coluna em um vetor

# Exibindo os resultados
print(f"x = {x}, y = {y}, z = {z}")