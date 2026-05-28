'''
Problema: beecrowd | 1051
Data: 2026.05.14
Estudante: Ian Forbeck
'''
#Objetivo: Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

# --- ANÁLISE (LIAC) ---
# Entrada: O usuário escreve o valor em float com duas casas
# Processamento: Calcula o valor do imposto baseado no valor que o usuário inseriu
# Saída: Mostra o valor do imposto ou se o imposto é isento

renda = float(input())

if renda <= 2000.00:
    print("Isento")
else:
    imposto = 0.0
    
    # Se a renda for maior que 4500
    if renda > 4500.00:
        imposto += (renda - 4500.00) * 0.28
        renda = 4500.00
    
    # Se a renda estiver na faixa entre 3000 e 4500
    if renda > 3000.00:
        imposto += (renda - 3000.00) * 0.18
        renda = 3000.00
        
    # Se a renda estiver na faixa entre 2000 e 3000
    if renda > 2000.00:
        imposto += (renda - 2000.00) * 0.08
        
    print(f"R$ {imposto:.2f}")