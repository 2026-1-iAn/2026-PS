'''
Problema: beecrowd | 1021 - Notas e Moedas
Data: 2026.04.30
Estudante: Ian Forbeck
'''
# Objetivo: Ler um valor monetário e decompô-lo no MENOR número possível
# de notas (100, 50, 20, 10, 5, 2, 1) e moedas (0.50, 0.25, 0.10, 0.05, 0.01)

# --- ANÁLISE (LIAC) ---
# Entrada: um valor monetário com 2 casas decimais (ex.: 576.73)
# Processamento: separar parte inteira (reais -> notas) e parte decimal (centavos -> moedas);
# usar divisão inteira (//) para descobrir QUANTAS unidades cabem
# e o resto da divisão (%) para guardar o que SOBROU para a próxima troca
# Saída: lista formatada de notas e moedas, na ordem do maior para o menor valor

# input() lê o valor como texto (ex.: "576.73"); split(".") corta no ponto
# e devolve uma LISTA com 2 pedaços: ["576", "73"]
# Atribuição múltipla -> n recebe o 1º pedaço (reais), m recebe o 2º pedaço (centavos)
n, m = input().split(".")

# Converte os pedaços de texto para inteiro, pois faremos contas com eles
n = int(n)  # reais (parte inteira do valor)
m = int(m)  # centavos (parte decimal)

# Decomposição dos REAIS em notas — sempre da maior para a menor:
# // é divisão INTEIRA (descarta o decimal) -> diz QUANTAS notas daquele valor cabem
# %  é o RESTO da divisão -> guarda o que sobrou para a próxima troca

n100 = n // 100;  n = n % 100    # quantas notas de 100 cabem; n vira o resto
n50  = n //  50;  n = n %  50    # quantas notas de 50 cabem no que sobrou
n20  = n //  20;  n = n %  20    # quantas notas de 20 cabem no que sobrou
n10  = n //  10;  n = n %  10    # quantas notas de 10 cabem no que sobrou
n05  = n //   5;  n = n %   5    # quantas notas de 5  cabem no que sobrou
n02  = n //   2;  n = n %   2    # quantas notas de 2  cabem no que sobrou
n01  = n                         # o que restou são notas de 1 real

# Decomposição dos CENTAVOS em moedas — mesma lógica, agora em centavos
# (50 centavos, 25 centavos, 10 centavos, 5 centavos, 1 centavo)
m50 = m // 50;  m = m % 50       # moedas de R$ 0,50
m25 = m // 25;  m = m % 25       # moedas de R$ 0,25
m10 = m // 10;  m = m % 10       # moedas de R$ 0,10
m05 = m //  5;  m = m %  5       # moedas de R$ 0,05
m01 = m                          # o que restou são moedas de R$ 0,01

# Saída formatada — exatamente como o juiz online espera (cuidado com a grafia!)
print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n05} nota(s) de R$ 5.00')
print(f'{n02} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{n01} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m05} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')