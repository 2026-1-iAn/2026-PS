# ============================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Pedra-Papel-Tesoura"
# Arquivo    : ppt.py
# Autor      : [Ian Forbeck]
# Data       : [16/06/2026]
# ============================================================

import random

# === Sub-rotina: decide o resultado de UMA rodada e devolve um texto ===
def resultado(jogador, maquina):
    # Testa caso a caso; o 1º return que bater já encerra a função
    if jogador == maquina:
        return "empate"
    if jogador == "pedra" and maquina == "tesoura":
        return "jogador"
    if jogador == "papel" and maquina == "pedra":
        return "jogador"
    if jogador == "tesoura" and maquina == "papel":
        return "jogador"
    return "maquina"  # nenhum acima -> a máquina venceu

# === Programa principal: joga as rodadas e cuida do placar ===
opcoes = ["pedra", "papel", "tesoura"]
pontos_jogador = 0
pontos_maquina = 0

for rodada in range(1, 6):
    print("--- Rodada", rodada, "---")
    jogada_maquina = random.choice(opcoes)
    # Leitura enxuta: ler + .lower() + .strip() em uma linha só
    jogada_jogador = input("Sua jogada: ").lower().strip()

    if jogada_jogador not in opcoes:
        print("❌ Inválida! Você perde a rodada.")
        pontos_maquina = pontos_maquina + 1
    else:
        quem = resultado(jogada_jogador, jogada_maquina)  # chamamos a sub-rotina
        if quem == "empate":
            print("🤝 Empate!")
        elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
        else:
            print("💀 A máquina ganhou a rodada!")
            pontos_maquina = pontos_maquina + 1

print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)