# =======================================
# Arquivo:      parimpar.py
# Disciplina:   2026-PCAP
# Aula:         23
# Autor:        Ian Forbeck
# Data:         2026.08.25
# Conceitos:    [Escreva depois]
# =======================================

import random
from telas import titulo, linha
from modulos import ler_numero, ler_opcao


def quem_venceu(soma, aposta):
    '''Retorna 'Jogador' ou 'Máquina' conforme o resultado da soma.'''
    resultado = "par" if soma % 2 == 0 else "impar"
    return "Jogador" if resultado == aposta else "Máquina"


def jogar_parimpar():
    '''Executa a partida de Par ou Ímpar (Melhor de 5).'''
    titulo("PAR OU ÍMPAR (Melhor de 5)")
    placar = {"Jogador": 0, "Máquina": 0}

    while placar["Jogador"] < 3 and placar["Máquina"] < 3:
        maquina = random.randint(0, 5)
        jogador = ler_numero("Escolha um número (0-5)", 0, 5)
        
        print("[1] Par | [2] Ímpar")
        aposta = "par" if ler_opcao("Aposta", ["1", "2"]) == "1" else "impar"

        soma = jogador + maquina
        vencedor = quem_venceu(soma, aposta)
        placar[vencedor] += 1

        print(f"Você: {jogador} | Máquina: {maquina} | Soma: {soma} ({'PAR' if soma % 2 == 0 else 'ÍMPAR'})")
        print(f"Vencedor da rodada: {vencedor}")
        print(f"Placar: {placar['Jogador']} x {placar['Máquina']}")
        linha()

    print("🎉 Você venceu!" if placar["Jogador"] == 3 else "💻 A máquina venceu!")
    linha()


if __name__ == '__main__':
    jogar_parimpar()