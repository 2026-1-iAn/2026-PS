'''
Problema: beecrowd | 1008
Data: 2026.04.13
Estudante: Ian Forbeck
'''

# Objetivo: Marcar e calcular número e valor total do salário 

# --- ANÁLISE (LIAC) ---
# Entrada: N = int(input())
##V = float(input())
# Processamento: SAL = H * V
# Saída: print(f"NUMBER = {N}")
#print(f"SALARY = U$ {SAL:.2f}")

# Leitura das entradas – observe o enunciado: quantas variáveis e de qual tipo?
N = int(input())
H = int(input())
V = float(input())

# Calcule o salário – use o 1009 como referência de estrutura
SAL = H * V

# Saída – observe o formato exato e o número de casas decimais no enunciado
print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")