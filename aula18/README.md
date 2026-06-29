# Jogo de Par ou Ímpar

## Descrição

Este projeto foi desenvolvido em Python como atividade da disciplina de Programação. O jogo consiste em uma disputa de **Par ou Ímpar** entre o jogador e a máquina.

A máquina escolhe um número aleatório entre **0 e 5**, enquanto o jogador escolhe um número no mesmo intervalo e aposta em **Par** ou **Ímpar**. Os dois números são somados e, dependendo do resultado, é definido o vencedor da rodada.

A partida é disputada em **melhor de cinco**, vencendo quem conquistar **3 vitórias primeiro**.

---

## Como o programa funciona

O programa utiliza a biblioteca `random` para gerar o número da máquina.

O código foi organizado em três funções principais:

### `quem_venceu(soma, aposta)`

Recebe a soma dos números e a aposta do jogador. Em seguida, verifica se o resultado é par ou ímpar e informa quem venceu a rodada.

### `jogar()`

Executa uma rodada completa do jogo. Nessa função:
- A máquina sorteia um número.
- O jogador escolhe um número entre 0 e 5.
- O jogador escolhe entre **Par** ou **Ímpar**.
- O programa calcula a soma dos números.
- O vencedor da rodada é exibido.

### `main()`

É a função principal do programa. Ela controla o placar, repete as rodadas até que alguém alcance **3 vitórias** e mostra o vencedor da partida.

---

## Conceitos utilizados

Durante o desenvolvimento foram utilizados os seguintes conceitos da linguagem Python:

- Importação de bibliotecas (`import random`)
- Variáveis
- Entrada e saída de dados (`input` e `print`)
- Estruturas condicionais (`if` e `else`)
- Estruturas de repetição (`while`)
- Funções (`def`)
- Retorno de valores (`return`)
- Operadores aritméticos (`+` e `%`)
- Modularização do código

---

## Como executar

Clique no ícone de inicializar, escolha seu número e se quer jogar com par ou ímpar.

## Autor: Ian Forbeck

Autoavaliação: 
Conceito pretendido: [ A ]

Justificativa: *Extensão/originalidade:* par_impar.py, linhas 65 a 93.
Além dos requisitos básicos, o projeto implementa as estatísticas do jogo.