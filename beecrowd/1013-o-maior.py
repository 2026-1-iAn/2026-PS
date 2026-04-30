'''
Problema: beecrowd | 1013 - O Maior
Data: 2026.04.30
Estudante: Ian Forbeck
'''
A, B, C = input().split()
# Recebe os valores
A = int(A)
B = int(B)
C = int(C)
# Transforma os valores em inteiros

MAIORAB = (A+B+abs(A-B)) // 2
# Calcula o  maior entre a e b

if MAIORAB > C:
    print(f"{MAIORAB} eh o maior")
else:
    print(f'{C} eh o maior')
# Mostra o maior dos numeros