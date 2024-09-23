import numpy as np

def is_positive_definite(matrix):
    """Verifica se a matriz é positiva definida."""
    if not np.allclose(matrix, matrix.T):
        return False  # A matriz deve ser simétrica
    eigenvalues = np.linalg.eigvals(matrix)
    return np.all(eigenvalues > 0)

def is_positive_semi_definite(matrix):
    """Verifica se a matriz é positiva semi-definida."""
    if not np.allclose(matrix, matrix.T):
        return False  # A matriz deve ser simétrica
    eigenvalues = np.linalg.eigvals(matrix)
    return np.all(eigenvalues >= 0)

# Exemplo de matriz armazenada em uma variável
A = np.array([[10, 2, 1],
              [2, 1, -2],
              [1, -2, 10]])

# Verificar se a matriz A é positiva definida ou semi-definida
if is_positive_definite(A):
    print("A matriz é positiva definida.")
elif is_positive_semi_definite(A):
    print("A matriz é positiva semi-definida.")
else:
    print("A matriz não é positiva definida nem semi-definida.")