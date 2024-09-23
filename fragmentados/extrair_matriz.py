import numpy as np
import re


def extrairMatrizeVetor():
    # Solicitar ao usuário o número de equações
    n_matriz = int(input("Digite o número de equações no sistema: "))

    # Inicializar a matriz de coeficientes e o vetor de constantes
    A = np.zeros((n_matriz, n_matriz))
    b = np.zeros(n_matriz)

    # Preencher a matriz de coeficientes e o vetor de constantes
    for i in range(n_matriz):
        equacao = input(f"\nDigite a equação {i + 1} (ex: '2x + 3y - z = 5'): ")

        # Separar os lados da equação
        esquerda, direita = equacao.split('=')
        direita = float(direita.strip())

        # Extrair os coeficientes da parte esquerda
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

        # Atribuir o valor da constante
        b[i] = direita

    return A, b


# Executar o programa
A, b = extrairMatrizeVetor()

print("\nMatriz de coeficientes A:")
print(A)
print("\nVetor de constantes b:")
print(b)