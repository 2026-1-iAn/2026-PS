## Data: 17/06/2026
## Jogo: Pedra-Papel-Tesoura
## Disciplina: PCAP

# Como jogar:

O jogador disputa uma partida de 5 rodadas contra a máquina. Em cada rodada:

O jogador escolhe entre pedra, papel ou tesoura;
A máquina faz uma escolha aleatória;
O vencedor da rodada é determinado pelas regras tradicionais do jogo;
O placar é atualizado automaticamente.

Ao final das rodadas, o programa exibe a pontuação final do jogador e da máquina.

# Regras do Jogo:

Pedra vence Tesoura;
Tesoura vence Papel;
Papel vence Pedra;
Escolhas iguais resultam em empate.

Caso o jogador digite uma opção inválida, a rodada é automaticamente atribuída à máquina.

# Pilares e Conceitos Utilizados

Este projeto utiliza diversos conceitos básicos da programação em Python:

Funções

Utilização da função resultado() para organizar a lógica do jogo e evitar repetição de código.

Estruturas Condicionais

Uso de if, elif e else para determinar o vencedor de cada rodada.

Laços de Repetição

Uso do for para controlar a quantidade de rodadas.

Listas

Armazenamento das opções válidas:

opcoes = ["pedra", "papel", "tesoura"]
Biblioteca Random

Uso do módulo random para gerar escolhas aleatórias da máquina:

random.choice(opcoes)
Validação de Entrada

Verificação das respostas do jogador para impedir entradas inválidas.

Variáveis e Contadores

Controle do placar através das variáveis:

pontos_jogador
pontos_maquina

## Autor: Ian Forbeck