'''
Problema: beecrowd | 1002
Data:2026.04.10
Estudante: Ian Forbeck
'''
#Objetivo: Calcular a área de um círculo e exibir com até 4 casas decimais

# --- ANÁLISE (LIAC) ---
# Entrada: um valor de ponto flutuante
# Processsamento: calcular a área usando AREA = pi*R**2
# Saída: a mensagem "A=" seguida pelo valor da área com até 4 casas após a vírgula

# Leitura do raio como número decimal
R = float(input())

# Defina pi onforme enunciado indica
pi = 3.14159

# Qual é a fórmula da área do círculo?
AREA = pi*R**2

# Saída - observe o formato exato e o número de casas decimais no enunciado
print(f"A={AREA:.4f}")