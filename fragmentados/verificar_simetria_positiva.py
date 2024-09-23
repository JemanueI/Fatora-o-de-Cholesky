import numpy as np

def is_positive_definite(matrix):
    """Verifica se a matriz é positiva definida."""
    eigenvalues = np.linalg.eigvals(matrix)
    return np.all(eigenvalues > 0)

def is_positive_semi_definite(matrix):
    """Verifica se a matriz é positiva semi-definida."""
    eigenvalues = np.linalg.eigvals(matrix)
    return np.all(eigenvalues >= 0)

# Exemplo de matriz armazenada em uma variável
A = np.array([[10, 2, 1],
              [2, 1, -2],
              [1, -2, 10]])

# Verificar se a matriz A é simétrica
if np.allclose(A, A.T):
    # Verificar se é positiva definida ou semi-definida
    if is_positive_definite(A):
        print("A matriz é simétrica e positiva definida.")
    elif is_positive_semi_definite(A):
        print("A matriz é simétrica e positiva semi-definida.")
    else:
        print("A matriz é simétrica, mas não é positiva.")
else:
    print("Não é simétrica nem positiva.")