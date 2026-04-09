'''
Problema: beecrowd | 1011
Data:2026.04.09
Estudante: Ian Forbeck
'''
#Objetivo: Ler o raio de uma esfera e calcular seu volume com a fórmula (4/3) * pi * R³

# --- ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante (o raio R)
# Processsamento: aplicar a fórmula do volume da esfera
# Saída: exibir no formato "VOLUME = valor" com 3 casas decimais

# float() -> converte o valor lido para número decimal (ponto flutuante)
R = float(input())

# O enunciado pede para atribuir pi como contante - não usar math.pi
pi = 3.14159

# 4.0/3 garant divisão decimal (não inteira) - coforme dica do enunciado
# R**3 -> R elevado a terceira potência (R³)
V = (4.0 / 3) * pi * R ** 3

# :.3f -> formata o número com exatamente 3 casas decimais
print(f"VOLUME = {V:.3f}")