'''
Problema: beecrowd | 1019
Data: 2026.04.13
Estudante: Ian Forbeck
'''

# Objetivo: Ler uma duração em segundos e convertê-la para horas:minutos:segundos

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro N representando segundos totais
# Processamento: extrair horas, minutos e segundos restantes por divisão inteira e módulo
# Saída: no formato h:m:s (sem zeros à esquerda - 0:9:16, não 00:09:16)

# int(input()) -> duração sempre é um número inteiro de segundos
N = int(input())

# // -> divisão inteira: retorna quantas vezes o divisor cabe no dividendo
# % -> módulo: retorna apenas o resto da divisão

# Quantas horas completas cabem em N segundos? (1 hora = 3600 segundos)
h = N // 3600

# Segundos restantes após retirar as horas completas
N = N % 3600

# Quantos minutos completos cabem nos segundos restantes? (1 minuto = 60 segundos)
m = N // 60

# Segundos que sobram após retirar os minutos completos
s = N % 60

# f-string monta o formato h:m:s - sem zeros à esquerda
print(f"{h}:{m}:{s}")