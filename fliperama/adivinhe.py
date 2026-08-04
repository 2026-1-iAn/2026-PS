# =======================================
# Arquivo:      adivinhe.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Ian Forbeck
# Data:         2026.08.04
# Conceitos:    [Escreva depois]
# =======================================

# importar bibliotecas e funções de arquivos (módulos)
from random import randint
from telas import titulo, linha
from modulos import ler_numero

def jogar_adivinhe():
    titulo('JOGO ADIVINHE O NÚMERO')
    print('Tente adivinhar o número que estou pensando entre 1 e 10.')
    segredo = randint(1, 10)
    tentativas = 0
    acertou = False
    
    while not acertou:
        palpite = ler_numero('Digite seu palpite', 1, 10)
        tentativas += 1
        
        if palpite < segredo:
            print('O número secreto é maior. Tente novamente.')
        elif palpite > segredo:
            print('O número secreto é menor. Tente novamente.')
        else:
            acertou = True
    else:
        linha()
        print(f'Parabéns! Você acertou o número secreto {segredo} em {tentativas} tentativas')    
    linha()