'''
Problema: beecrowd | 1037
Data: 2026.04.23
Estudante: Ian Forbeck
'''

# Objetivo: Ler um valor float e indicar em qual intervalo ele se encontra

# --- ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante qualquer
# Processamento: verificar em qual dos intervalos o valor se enquadra
# [0,25]   -> 0 <= valor <= 25
# (25,50]  -> 25 < valor <= 50
# (50,75]  -> 50 < valor <= 75
# (75,100] -> 75 < valor <= 100
# fora     -> qualquer outro valor
# Saída: mensagem com o intervalo correspondente ou "Fora de intervalo"

valor = float(input())

# Cada elif só é testado se todas as condições anteriores forem falsas
# Isso elimina a necessidade de ifs aninhados - código mais limpo e legível
if 0 <= valor <= 25:
    # Colchete [ indica que o extremo está incluído no intervalo
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    # Parêntese ( indica que 25 não está incluído - apenas valores maiores que 25
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    # Nenhum intervalo correspondeu: valor negativo ou acima de 100
    print("Fora de intervalo")