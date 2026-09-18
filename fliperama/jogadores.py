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


def cadastrar(jogadores):
    '''
    Pergunta apelido e nome e acrescenta um jogador ao cadastro.
    Garante que o apelido nao tenha espacos, nao esteja em branco
    e nao seja repetido no sistema.
    
    Nao devolve nada: o cadastro muda no lugar.
    '''
    titulo('NOVO JOGADOR')

    while True:
        apelido = ler_texto('Apelido (sem espaços)').lower()
        if ' ' in apelido:
            print('O apelido não pode conter espaços! Tente novamente.')
        elif buscar(jogadores, apelido) != -1:
            print('Apelido já cadastrado! Escolha outro.')
        else:
            break

    nome = ler_texto('Nome completo')

    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador ' + apelido + ' cadastrado.')
    linha()
    return apelido


def listar(jogadores):
    titulo('TOP 10 JOGADORES')

    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado ainda.")
    else:
        # Ordena por partidas (índice 2) em ordem decrescente (Critério E14)
        jogadores_ordenados = sorted(jogadores, key=lambda j: int(j[2]), reverse=True)
        top10 = jogadores_ordenados[:10]

        for pos, jogador in enumerate(top10, start=1):
            print(f"{pos:2d}º | {jogador[0]} | {jogador[1]} | {jogador[2]} partidas")

    linha()


def alterar(jogadores):
    listar(jogadores)

    if len(jogadores) == 0:
        return

    # Usando ler_texto para recusar entradas em branco (Critério E4)
    apelido = ler_texto('Apelido de quem vai mudar de nome').lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Nao achei ninguem com esse apelido.')
    else:
        print('Nome atual: ' + jogadores[i][1])
        jogadores[i][1] = ler_texto('Nome novo')
        print("Pronto. Agora é " + jogadores[i][1] + '.')

    linha()


def excluir(jogadores):
    '''
    Exclui um jogador do cadastro, solicitando confirmacao ao usuario.
    Verifica se o apelido existe antes de prosseguir.
    '''
    listar(jogadores)

    if len(jogadores) == 0:
        return

    apelido = ler_texto('Apelido de quem vai sair do cadastro').lower()
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
    arquivo = open(ARQUIVO, 'w', encoding='utf-8')

    for jogador in jogadores:
        arquivo.write(jogador[0] + ',' + jogador[1] + ',' + jogador[2] + '\n')

    arquivo.close()


def carregar_jogadores():
    if not exists(ARQUIVO):
        return []

    arquivo = open(ARQUIVO, 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()

    lidos = []
    for linha_lida in linhas:
        campos = linha_lida.strip().split(',')
        if len(campos) == 3:
            lidos.append(campos)

    return lidos


def menu_jogadores(jogadores):
    while True:
        titulo('CADASTRO DE JOGADORES')
        print('[1] Cadastrar jogador')
        print('[2] Listar Top 10')
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
    titulo('IDENTIFICAÇÃO DO JOGADOR')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado no sistema. Vamos cadastrar você!')
        linha()
        apelido = cadastrar(jogadores)
        return apelido

    while True:
        apelido = ler_texto('Digite seu apelido de jogador').lower()
        pos = buscar(jogadores, apelido)
        
        if pos != -1:
            print(f'Bem-vindo(a) de volta, {jogadores[pos][1]}!')
            linha()
            return apelido
        else:
            print('Apelido não encontrado! Tente novamente.')


def incrementar_partida(jogadores, apelido):
    pos = buscar(jogadores, apelido)
    if pos != -1:
        partidas = int(jogadores[pos][2]) + 1
        jogadores[pos][2] = str(partidas)