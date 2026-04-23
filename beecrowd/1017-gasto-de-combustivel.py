'''
Problema: beecrowd | 1017
Data: 2026.04.23
Estudante: Ian Forbeck
'''

# Objetivo: 

# --- ANÁLISE (LIAC) ---
# Entrada: dois inteiros - um para receber o valor de tempo e o outro para  receber o valor de velocidade média
# Processamento: quantidade de L necessarios para fazer uma viagem -> horasdeviagem * Vm / 12  
# Saída: mostrar quantidade de litros de cumbustivel gastos em uma viagem

horasdeviagem = int(input())
# A váriavel "horas de viagem" recebe o valor de tempo (em horas)

Vm = int(input())
# A váriavel "Vm" recebe o valor de velocidade média (em km/h)

print(f"{horasdeviagem * Vm / 12:.3f}")