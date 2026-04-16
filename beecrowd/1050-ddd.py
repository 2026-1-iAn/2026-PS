'''
Problema: beecrowd | 1050
Data: 2026.04.13
Estudante: Ian Forbeck
'''

# Objetivo: Ler um código DDD e informar a qual cidade ele pertence

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro representando o código DDD
# Processamento: comparar o DDD lido com cada código da tabela usando if/elif/else
# Saída: nome da cidade correspondente, ou "DDD nao cadastrado" se não encontrado

# int(input()) -> DDD é sempre um número inteiro
DDD = int(input())

# Estrutura if/elif/else: testa cada condição em sequência
# Apenas o primeiro bloco verdadeiro é executado - os demais são ignorados
if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("Sao Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else:
    # Nenhuma condição acima foi verdadeira -> DDD não está na tabela
    print("DDD nao cadastrado")