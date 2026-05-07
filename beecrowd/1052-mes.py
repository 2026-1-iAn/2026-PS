'''
Problema: beecrowd | 1052
Data: 2026.05.07
Estudante: Ian Forbeck
'''

# Objetivo: Trocar um n° por um mês em inglês

# --- ANÁLISE (LIAC) ---
# Entrada: A entrada contém um único valor inteiro
# Processamento: 
# Saída: Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

x = int(input())

if x == 1:
    print('January')
elif x == 2:
    print("February")
elif x == 3:
    print("March")
elif x == 4:
    print("April")
elif x == 5:
    print("May")
elif x == 6:
    print("June")
elif x == 7:
    print("July")
elif x == 8:
    print("August")
elif x == 9:
    print("September")
elif x == 10:
    print("October")
elif x == 11:
    print("November")
elif x == 12:
    print("December")