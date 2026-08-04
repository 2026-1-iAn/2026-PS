# =======================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Ian Forbeck
# Data:         2026.08.04
# Conceitos:    [Escreva depois]
# =======================================

# Importar funções de arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao

NOME_DO_DONO = 'IAN FORBECK'
OPCOES = ['0', '1']

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Número')
    print('0 - Sair do Fliperama')
    linha()
    opcao = input('Escolha uma opção: ').strip()
    
    if opcao == '0':
        print('Até a Próxima!')
        break
    elif opcao == '1':
        jogar_adivinhe()
