# =======================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Ian Forbeck
# Data:         2026.08.04
# Conceitos:    Menu principal, gerenciamento de estado e fluxo do app
# =======================================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores, selecionar_jogador, incrementar_partida
from senhasecreta import jogar_senhasecreta

NOME_DO_DONO = 'IAN FORBECK'
NOMES_DOS_JOGOS = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar', 'Senha Secreta']

vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

# Solicita a identificação do jogador no início do sistema
jogador_atual = selecionar_jogador(jogadores)


def mostrar_placar():
    titulo('PLACAR')
    for i in range(len(NOMES_DOS_JOGOS)):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')
    linha()


while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('[5] - Jogadores')
    print('[4] - Senha Secreta (Jogo Autoral)')
    print('[3] - Par ou Ímpar')
    print('[2] - Pedra - Papel - Tesoura')
    print('[1] - Jogo Adivinhe o Número')
    print('[0] - Sair do Fliperama')
    linha()

    opcao = ler_opcao('Escolha uma opção', ['0', '1', '2', '3', '4', '5'])

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo('Ate a proxima!')
        break

    elif opcao == '5':
        # Abre menu de jogadores sem interferir no placar dos jogos
        menu_jogadores(jogadores)

    else:
        # Executado apenas para os jogos (opções 1, 2, 3 e 4)
        indice = int(opcao) - 1
        vezes_jogado[indice] += 1
        
        # Incrementa +1 partida para o perfil do jogador
        incrementar_partida(jogadores, jogador_atual)

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao == '3':
            jogar_parimpar()
        elif opcao == '4':
            jogar_senhasecreta()

        input('Pressione Enter para voltar ao menu... ')