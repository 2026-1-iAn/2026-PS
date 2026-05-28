'''
Problema: beecrowd | 1036
Data: 2026.05.14
Estudante: Ian Forbeck
'''
#Objetivo: Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# --- ANÁLISE (LIAC) ---
# Entrada: Ler três valores de ponto flutuante (double) A, B e C.
# Processamento: 
# Saída: Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.

import math

try:
    linha = input().split()
    A = float(linha[0])
    B = float(linha[1])
    C = float(linha[2])

    # Cálculo do Delta (discriminante)
    delta = (B ** 2) - (4 * A * C)

    # Verificação das condições de erro:
    # 1. Se A for 0, ocorrerá divisão por zero (2 * A)
    # 2. Se delta for negativo, não há raiz real
    if A == 0 or delta < 0:
        print("Impossivel calcular")
    else:
        # Cálculo das duas raízes
        r1 = (-B + math.sqrt(delta)) / (2 * A)
        r2 = (-B - math.sqrt(delta)) / (2 * A)

        # Exibe o resultado com 5 casas decimais
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
        
except EOFError:
    pass