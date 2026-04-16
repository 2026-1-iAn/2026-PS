'''
Problema: beecrowd | 1007
Data: 2026.04.16
Estudante: Ian Forbeck
'''
# Objetivo: Ler quatro inteiros e calcular DIFERENCA = (A * B) - (C * D)

# --- ANÁLISE (LIAC) ---
# Entrada: quatro valores inteiros A, B, C, e D (um por linha)
# Processamento: diferença entre o produto A*B e o produto C*D
# Saída: "DIFERENCA = valor" (inteiro, letras maiúsculas, espaços ao redor do =)

A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Calcula a diferença dos produtos conforme a fórmula do enunciado
dif = (A * B) - (C * D)

print(f"DIFERENCA = {dif}")