'''
Problema: beecrowd | 1038
Data: 2026.05.014
Estudante: Ian Forbeck
'''

# Objetivo: Escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
# --- ANÁLISE (LIAC) ---
# Entrada: O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
# Processamento: Calcula o total utilizando a fórmula: total = preco * quantidade 
# Saída: O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

# Lê a linha de entrada e divide os dois valores
entrada = input().split()
codigo = int(entrada[0])
quantidade = int(entrada[1])

# Estrutura de decisão para definir o preço com base no código
if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50

# Calcula o valor total
total = preco * quantidade

# Exibe o resultado formatado com 2 casas decimais
print(f"Total: R$ {total:.2f}")