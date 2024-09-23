def transposta(matriz):
    # Usando compreensão de lista para calcular a transposta
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Exemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_transposta = transposta(matriz)

print("Matriz Original:")
for linha in matriz:
    print(linha)

print("\nMatriz Transposta:")
for linha in matriz_transposta:
    print(linha)
