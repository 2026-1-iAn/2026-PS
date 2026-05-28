'''
Problema: beecrowd | 1004
Data:2026.04.09
Estudante: Ian Forbeck
'''
#Objetivo: Ler dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.   

# --- ANÁLISE (LIAC) ---
# Entrada: O arquivo de entrada contém 2 valores inteiros.
# Processsamento: Para chegar a variável PROD, utilizo a fórmula PROD = A * B
# Saída: Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

A = int(input())
B = int(input())

# Qual operação o enunciado pede?
PROD = A * B

# Saída - observe o formato exato no enunciado
print(f"PROD = {A*B}")