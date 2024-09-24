import numpy as np
import re

def sistemaLinear():
    n = int(input("Digite o número de equações (ou variáveis): "))

    A = []
    b = []

    for i in range(n):
        equacao = input(f"\nDigite a {i + 1}ª equação: ")

        partes = re.split(r'[\s=]+', equacao)

        coeficientes = []
        for j in range(n):
            match = re.search(r'([-+]?\d*\.?\d*)x' + str(j + 1), equacao)
            if match:
                coeficientes.append(float(match.group(1)) if match.group(1) != '' else 1.0)
            else:
                coeficientes.append(0.0)
        A.append(coeficientes)

        b.append(float(partes[-1]))

    return np.array(A), np.array(b)

def verificarQuadrada(matriz):
    return matriz.shape[0] == matriz.shape[1]
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
            if i == j:
                G[i, j] = np.sqrt(matriz[i, i] - np.sum(G[i, :j] ** 2))
            else:
                G[i, j] = (matriz[i, j] - np.sum(G[i, :j] * G[j, :j])) / G[j, j]

    return G

def transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def multiplicacaoMatriz(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

def verificarIgualdade(matrizResultado, matrizComparacao):
    return np.array_equal(matrizResultado, matrizComparacao)

def calcularMatrizColuna(matriz1, matriz2):

    if np.linalg.det(matriz1) == 0:
        return "\nA matriz G não é invertível."

    Y = np.linalg.solve(matriz1, matriz2)
    return Y

def main():
    A, b = sistemaLinear()

    print("\nMatriz A:")
    print(A)

    print("\nMatriz coluna b:")
    print(b)

    if verificarQuadrada(A):
        print("\nA matriz 'A' é quadrada.")

        if np.allclose(A, A.T):
            if verificarPositiva(A):
                print("\nA matriz 'A' é simétrica e positiva.")

                G = calcularTriangularInferior(A)
                print("\nA matriz triangular inferior ('G'):\n", G)

                G_T = transposta(G)
                print("\nA matriz triangular superior ('G_T'):\n", G_T)

                resultado = multiplicacaoMatriz(G, G_T)
                print("\nA matriz resultado de 'G*G_T':\n", resultado)

                if verificarIgualdade(resultado, A):
                    print("\nO resultado da multiplicação é igual à matriz A.")

                    matriz_Y = calcularMatrizColuna(G, b)

                    if isinstance(matriz_Y, str):
                        print(matriz_Y)
                    else:
                        print("\nA matriz coluna dos valores de Y:", matriz_Y)

                        matriz_X = calcularMatrizColuna(G_T, matriz_Y)

                        if isinstance(matriz_X, str):
                            print(matriz_X)
                        else:
                            print("\nA matriz coluna dos valores de X:", matriz_X)
                else:
                    print("\nO resultado da multiplicação G * G_T não é igual à matriz A.")

            else:
                print("\nA matriz 'A' é simétrica, mas não é positiva.")
        else:
            print("\nA matriz 'A' não é simétrica nem positiva.")
    else:
        print("\nA matriz 'A' não é quadrada.")

if __name__ == '__main__':
    main()
