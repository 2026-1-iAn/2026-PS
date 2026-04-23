'''
Problema: beecrowd | 1010
Data: 2026.04.23
Estudante: Ian Forbeck
'''
#Objetivo: Ler código, quantidade e valor unitário de duas peças e calcular o total a pagar

# --- ANÁLISE (LIAC) ---
# Entrada: duas linhas; cada uma com código (int), quantidade (int) e valor unitário (float
# Processamento: total = () + ()
# Saída: "VALOR A PAGAR: R$ " com casas decimais 

# Lê a primeira linha e separa os três valores pelo espaço
cod1, qtd1, val1 = input().split()

# Converte quantidade para inteiro e valor unitário para float
qtd1 = int(qtd1)
val1 = float(val1)

#Lê a segunda linha e separa os três valores pelo espaço
cod2, qtd2, val2 = input().split()

# Converte quantidade para inteiro e valor unitário para float
qtd2 = int(qtd2)
val2 = float(val2)

#calcula o valor total:subtotal da peça 1 + subtotal da peça 2
total = (qtd1*val1) + (qtd2*val2)

#exibe o resultado no formato exato exigido pelo enunciado
print (f"VALOR A PAGAR: R$ {total:.2f}")