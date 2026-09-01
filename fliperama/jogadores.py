# ===================================================================
# ARQUIVO    : jogadores.py (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 23 - MiniApp v2.0: o cadastro de jogadores.
# Autor      : Ian Forbeck
# Revisado   : Aula 23 - validacao de campo vazio e documentacao
# Conceitos  : Registro como lista de campos, cadastro como lista
#              de listas, cadastrar, listar, buscar, alterar,
#              excluir, persistencia em arquivo .csv
# ===================================================================
# 
# O QUE FAZ ESTE ARQUIVO ?
#    A quarta gaveta do projeto. O telas.py cuida do que APARECE,
#    o modulos.py cuida do que o programa PERGUNTA, o placar.py
#    cuida de quantas partidas cada jogo teve, e o jogadores.py
#    cuida de QUEM joga.
#
# O REGISTRO
#    Cada jogador e uma lista de tres campos, sempre nesta ordem:
#        indice 0 -> apelido | 1 -> nome | 2 -> partidas
#    E o cadastro e uma lista dessas listas.
# ===================================================================

from os.path import exists
from telas import titulo, linha
from modulos import ler_opcao, ler_texto

ARQUIVO = 'jogadores.csv'


def cadastrar(jogadores):
    '''
    Pergunta apelido e nome e acrescenta um jogador ao cadastro.
    
    Nao devolve nada: o cadastro muda no lugar
    '''
    titulo('NOVO JOGADOR')

    apelido = ler_texto('Apelido (sem espaços): ').lower()
    nome = ler_texto('Nome completo: ')

    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador ' + apelido + ' cadastrado.')
    linha()


def listar(jogadores):
    titulo('JOGADORES CADASTRADOS')

    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado ainda.")
    else:
        for jogador in jogadores:
            print(jogador[0] + " | " + jogador[1] + " | " + jogador[2] + " partidas ")

    linha()           


def buscar(jogadores, apelido):
    '''
    Procura um apelido no cadastro e diz ONDE ele esta.
    
    Parametros:
        jogadores   (list) - o cadastro inteiro
        apelido     (str)  - o apelido procurado, em minusculas
    
    Retorno:
        int - a posicao do jogador na lista, ou -1 se nao achar
    '''
    for i in range(len(jogadores)):
        if jogadores[i][0] == apelido:
            return i

    return -1    

def alterar(jogadores):
    listar(jogadores)

    apelido = input('Apelido de quem vai mudar de nome: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Nao achei ninguem com esse apelido.')
    else:
        print('Nome atual: ' + jogadores[i][1])
        jogadores[i][1] = input('Nome novo: ').strip()
        print("pronto. Agora e " + jogadores[i][1] + '.')   

    linha()



def excluir(jogadores):
    '''
    Exclui um jogador mas pede ao usuário para confirmar a decisão.
    '''
    listar(jogadores)

    apelido = input('Apelido de quem vai sair do cadastro: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Nao achei ninguem com esse apelido.')
    else:
        print('Vou apagar o cadastro de ' + jogadores[i][1] + '.')
        print('[1] Confirmar')
        print('[2] Deixar como esta')
        certeza = ler_opcao('Sua escolha', ['1', '2'])

        if certeza == '1':
            jogadores.pop(i)
            print('Cadastro apagado.')
        else:
            print('Nada foi apagado.')

    linha()


def salvar_jogadores(jogadores):
    arquivo = open(ARQUIVO, 'w')

    for jogador in jogadores:
        arquivo.write(jogador[0] + ',' + jogador[1] + ',' + jogador[2] + '\n')

    arquivo.close()


def carregar_jogadores():
    if not exists(ARQUIVO):
        return []

    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    lidos = []
    for linha_lida in linhas:
        campos = linha_lida.strip().split(',')
        lidos.append(campos)

    return lidos


def menu_jogadores(jogadores):
    while True:
        titulo('CADASTRO DE JOGADORES')
        print('[1] Cadastrar jogador')
        print('[2] Listar jogadores')
        print('[3] Alterar nome')
        print('[4] Excluir jogador')
        print('[0] Voltar ao fliperama')
        linha()

        opcao = ler_opcao('Sua escolha', ['0', '1', '2', '3', '4'])

        if opcao == '0':
            break
        elif opcao == '1':
            cadastrar(jogadores)
        elif opcao == '2':
            listar(jogadores)
        elif opcao == '3':
            alterar(jogadores)
        else:
            excluir(jogadores)
            
def selecionar_jogador(jogadores):
    '''
    Solicita o apelido do jogador atual.
    Caso não exista nenhum jogador cadastrado, força a realização do cadastro.
    '''
    titulo('IDENTIFICAÇÃO DO JOGADOR')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado no sistema. Vamos cadastrar você!')
        linha()
        apelido = cadastrar(jogadores)
        return apelido

    while True:
        apelido = input('Digite seu apelido de jogador: ').strip().lower()
        pos = buscar(jogadores, apelido)
        
        if pos != -1:
            print(f'Bem-vindo(a) de volta, {jogadores[pos][1]}!')
            linha()
            return apelido
        else:
            print('Apelido não encontrado! Tente novamente.')


def incrementar_partida(jogadores, apelido):
    '''
    Soma 1 à contagem de partidas jogadas pelo jogador identificado.
    '''
    pos = buscar(jogadores, apelido)
    if pos != -1:
        partidas = int(jogadores[pos][2]) + 1
        jogadores[pos][2] = str(partidas)