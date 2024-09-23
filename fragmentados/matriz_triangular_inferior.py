import numpy as np


def cholesky_decomposition(A):
    """Realiza a fatoração de Cholesky de uma matriz positiva definida."""
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i + 1):
            if i == j:  # diagonal
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j] ** 2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]

    return L


# Exemplo de uso
A = np.array([[4, 2, 2],
              [2, 2, 0],
              [2, 0, 2]])

print("Matriz original A:")
print(A)

L = cholesky_decomposition(A)

print("\nMatriz triangular inferior L:")
print(L)

# Verificando se A = L @ L.T
print("\nVerificação de A = L * L^T:")
print(np.allclose(A, L @ L.T))