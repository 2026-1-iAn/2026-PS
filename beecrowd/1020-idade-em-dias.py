'''
Problema: beecrowd | 1020
Data: 2026.05.07
Estudante: Ian Forbeck
'''

# Objetivo: Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# --- ANÁLISE (LIAC) ---
# Entrada: O arquivo de entrada contém um valor inteiro
# Processamento: // e % 
# Saída: Imprima a saída conforme exemplo fornecido

D = int(input())
# Recebe o número de dias

a = D // 365
# a é a quantidade de anos que foi convertida de dias para anos

D = D % 365 
# Recebe quantos dias sobraram do ano

m = D // 30
# Calcula os dias que sobraram em meses

d = D % 30
# Mostra os dias que sobraram dos meses

print(f"{a} ano(s)")
# Mostra os anos

print(f"{m} mes(es)")
# Mostra os meses

print(f"{d} dia(s)")
# Mostra os dias