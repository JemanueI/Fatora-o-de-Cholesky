import numpy as np
import re


def extrairMatrizeVetor():
    n_matriz = int(input("Digite o número de equações no sistema: "))

    A = np.zeros((n_matriz, n_matriz))
    b = np.zeros(n_matriz)

    for i in range(n_matriz):
        equacao = input(f"\nDigite a equação {i + 1} (ex: '2x + 3y - z = 5'): ")

        esquerda, direita = equacao.split('=')
        direita = float(direita.strip())

        termos = re.findall(r'([+-]?\d*\.?\d*[xyzw]?)', esquerda)

        for termo in termos:
            if 'x' in termo:
                coef = termo.replace('x', '').strip()
                coef = float(coef) if coef not in ('', '+', '-') else float(coef + '1')
                A[i, 0] = coef
            elif 'y' in termo:
                coef = termo.replace('y', '').strip()
                coef = float(coef) if coef not in ('', '+', '-') else float(coef + '1')
                A[i, 1] = coef
            elif 'z' in termo:
                coef = termo.replace('z', '').strip()
                coef = float(coef) if coef not in ('', '+', '-') else float(coef + '1')
                A[i, 2] = coef

        b[i] = direita

    return A, b
def verificarPositiva(matriz):
    if not np.allclose(matriz, matriz.T):
        return False
    autovalores = np.linalg.eigvals(matriz)
    return np.all(autovalores > 0)

def calcularTriangularInferior(matriz):
    n = matriz.shape[0]
    G = np.zeros_like(matriz)

    for i in range(n):
        for j in range(i + 1):
            if i == j:  # diagonal
                G[i, j] = np.sqrt(matriz[i, i] - np.sum(G[i, :j] ** 2))
            else:
                G[i, j] = (matriz[i, j] - np.sum(G[i, :j] * G[j, :j])) / G[j, j]

    return G

def transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def main():
    A, b = extrairMatrizeVetor()

    print(A)

    if np.allclose(A, A.T):
        if verificarPositiva(A):
            print("A matriz é simétrica e positiva definida.")

            print(A)

            G = calcularTriangularInferior(A)
            print(G)

            G_T = transposta(G)
            print(G_T)
        else:
            print("A matriz é simétrica, mas não é positiva.")
    else:
        print("Não é simétrica nem positiva.")

if __name__ == '__main__':
    main()