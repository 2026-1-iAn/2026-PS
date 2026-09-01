# ===================================================================
# ARQUIVO                : senhasecreta.py (pasta fliperama)
# Autor                  : Ian Forbeck
# Conceitos              : Jogo de adivinhação simplificado de 3 dígitos
# Funções importadas     : telas.py (titulo, linha) e modulos.py (ler_texto)
# Data                   : 2026.09.01
# ===================================================================

from random import sample
from telas import titulo, linha
from modulos import ler_texto


def jogar_senhasecreta():
    titulo('SENHA SECRETA')
    print('Adivinhe a senha de 3 números (de 0 a 9) sem repetir!')
    print('Dicas após cada palpite:')
    print(' - Na posição certa: número e lugar corretos.')
    print(' - Existe na senha: o número está na senha, mas no lugar errado.')
    linha()

    # Gera 3 números diferentes aleatórios (ex: ['1', '5', '8'])
    senha = sample([str(n) for n in range(10)], 3)
    tentativas = 10

    for rodada in range(1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}')
        
        # Leitura simples usando a função ler_texto de modulos.py
        while True:
            palpite = ler_texto('Digite 3 números').strip()
            if len(palpite) == 3 and palpite.isdigit():
                break
            print('Atenção: digite exatamente 3 números! Exemplo: 123')

        # Contagem de acertos
        certos = 0
        existem = 0

        for i in range(3):
            if palpite[i] == senha[i]:
                certos += 1
            elif palpite[i] in senha:
                existem += 1

        print(f'-> Na posição certa: {certos}')
        print(f'-> Apenas existe na senha: {existem}')
        linha()

        if certos == 3:
            titulo('VOCÊ VENCEU!')
            print(f'Parabéns! Você descobriu a senha {"".join(senha)}!')
            linha()
            return

    titulo('FIM DE JOGO')
    print(f'Que pena, suas tentativas acabaram!')
    print(f'A senha secreta era: {"".join(senha)}')
    linha()