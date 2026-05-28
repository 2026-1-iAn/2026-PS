'''
Problema beecrowd | 1015 
Data: 2026.05.14
Estudante: Ian Forbeck
'''
# Objetivo: Calcular a distancia entre dosi pontos determinados pelo usuário

# --- ANÁLISE (LIAC) ---
#Entrada:usuário digita diferentes valores em float 
# Processamento:Calcula a distancia com a fórmula dada no problema
# Saída:imprime o valor da distancia com 4 numeros depois do zero

import math

linha1 = input().split()
x1 = float(linha1[0])
y1 = float(linha1[1])


linha2 = input().split()
x2 = float(linha2[0])
y2 = float(linha2[1])

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")