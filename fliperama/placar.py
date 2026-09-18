# ===============================================================
# Arquivo:      placar.py (pasta fliperama)
# Conceitos:    Arquivo de texto, modo de abertura, write, close
# Autor:        Ian Forbeck
# ===============================================================

from os.path import exists

ARQUIVO = 'placar.csv'
NOMES = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar', 'Senha Secreta']


def salvar_placar(vezes):
    arquivo = open(ARQUIVO, 'w', encoding='utf-8')
    for i in range(len(NOMES)):
        arquivo.write(NOMES[i] + ',' + str(vezes[i]) + '\n')
    arquivo.close()


def carregar_placar():
    if not exists(ARQUIVO):
        return [0, 0, 0, 0]

    arquivo = open(ARQUIVO, 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()

    vezes = []
    for linha_lida in linhas:
        pedacos = linha_lida.strip().split(',')
        if len(pedacos) >= 2:
            vezes.append(int(pedacos[1]))

    # Garante tamanho de lista compatível com os 4 jogos
    while len(vezes) < 4:
        vezes.append(0)

    return vezes[:4]