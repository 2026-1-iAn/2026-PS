'''
Problema: beecrowd | 1046 – Tempo de Jogo com Minutos
Data: 2026.04.30
Estudante: Ian Forbeck
'''
# Objetivo: Calcular a DURAÇÃO de um jogo (em horas e minutos), sabendo
# a hora de início (hi:mi) e a hora de fim (hf:mf).
# O jogo dura no MÍNIMO 1 minuto e no MÁXIMO 24 horas.

# --- ANÁLISE (LIAC) ---
# Entrada: 4 inteiros na MESMA linha -> hi mi hf mf (hora/minuto inicial e final)
# Processamento: converter início e fim para o total em MINUTOS;
# se o fim for menor ou igual ao início, o jogo "virou a meia-noite"
# (somar 24h em minutos); converter a duração de volta para horas e minutos
# Saída: "O JOGO DUROU H HORA(S) E M MINUTO(S)"

# input().split() lê a linha e a quebra em pedaços por ESPAÇO -> ["16","00","7","00"]
# map(int, ...) aplica int() em CADA pedaço de uma vez -> vira [16, 0, 7,0]
# Os 4 valores são desempacotados nas 4 variáveis na ordem
hi, hf = map(int, input().split())

# Converte tudo para MINUTOS – fica MUITO mais fácil calcular duração
# trabalhando em uma única unidade do que em horas+minutos separados
tim = (hi * 60)    # Tempo Inicial em Minutos
tfm = (hf * 60)    # Tempo Final em Minutos

# Se o início é MAIOR que o fim, o jogo passou da meia-noite
# (ex.: começou 23:00 e terminou 02:00 do dia seguinte)
# Nesse caso somamos 24h (24 * 60 minutos) à duração para "fechar a volta"
if tim >= tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim    # caso normal: duração = fim - início

# Caso especial: início == fim -> o enunciado diz que o jogo dura 24 horas
# (porque a duração mínima é 1 min e a máxima é 24h, então 0 vira 24h)
if ttm == 0:
    ttm = 24 * 60

# Converte a duração total de minutos de volta para horas e minutos
# ttm // 60 -> divisão inteira->quantas horas COMPLETAS cabem
# ttm % 60 -> resto -> minutos que sobraram
print(f"O JOGO DUROU {ttm // 60} HORA(S)")