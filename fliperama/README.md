# Fliperama do Ian Forbeck

Um fliperama com quatro jogos, placar persistente e cadastro de jogadores. Projeto da disciplina PCAP, 1º ano do Técnico em Informática do IFPR.

## O que ele faz

* **Quatro jogos no menu:** Adivinhe o Número, Pedra-Papel-Tesoura, Par ou Ímpar e Senha Secreta (Jogo Autoral).
* **Placar Persistente:** Conta as partidas de cada jogo e mantém os dados gravados ao fechar o programa.
* **Cadastro Completo de Jogadores:** Operações CRUD (cadastrar, listar Top 10, alterar e excluir) com persistência em CSV.

## Como rodar

cd fliperama
python3 main.py


## Autoavaliação

**Conceito Pretendido:** Conceito B


Creio que cumpri todas as especificações do Conceito B na tabela de critérios de avaliação presente na Atividade 15; Aula 21.

# Critérios
1. Estrutura e registro:

docstrings nas funções: buscar; cadastrar; listar; alterar; excluir; salvar_jogadores; carregar_jogadores; menu_jogadores; selecionar_jogador; incrementar_partida.
linhas: 33; 50; 79; 102; 129; 162; 178; 202; 232; 264.
arquivo: jogadores.py

2. As quatro operações:

# O código pergunta quem vai jogar:
linha: 25/26

arquivo: main.py

main.py (linha 25): Executa a chamada jogador_atual = selecionar_jogador(jogadores) logo na inicialização do sistema.

linha: 174 a 192 (def selecionar_jogador)

arquivo: jogadores.py

jogadores.py (linhas 174 a 192): Contém a função selecionar_jogador, responsável por perguntar o apelido do jogador e validar se ele já existe no cadastro.

# O código soma 1 no campo 'partidas' da pessoa certa:
linha: 64/65

arquivo: main.py

main.py (linha 63): Executa a chamada incrementar_partida(jogadores, jogador_atual) assim que o usuário escolhe qualquer um dos 4 jogos no menu.

linha: 195 a 199 (def incrementar_partida)

arquivo: jogadores.py

jogadores.py (linhas 195 a 199): Contém a função incrementar_partida, que localiza a posição do jogador atual via buscar e faz +1 na contagem de partidas (índice 2).

3. Busca e índice:

# A busca devolve posição ou -1; alterar e excluir conferem antes de usar:

linha: 33 a 44 (def buscar), 114-118 (alterar) e 138-142 (excluir)

arquivo: jogadores.py

jogadores.py: A buscar retorna a posição ou -1. As funções alterar e excluir checam if i == -1: para não alterar nem apagar ninguém por engano.

# Conferência do -1 no login e jogo abrindo sem cadastro:

linha: 241 a 252 (def selecionar_jogador)

arquivo: jogadores.py

jogadores.py: Valida if pos != -1: no login. Se não achar, permite tentar de novo ou cadastrar na hora sem travar.

# Explicação no README.md do porquê -1 não é zero:

linha: Seção ## Busca e Índice

arquivo: README.md

README.md: Explica que -1 significa "não encontrado", pois o índice 0 é o primeiro jogador. Sem o if, o programa alteraria/apagaria o primeiro da lista.

4. Persistência e primeira execução:
# Programa abre sem erro sem o arquivo jogadores.csv:

linha: 178 a 180 (def carregar_jogadores)

arquivo: jogadores.py

jogadores.py: O if not exists(ARQUIVO): return [] evita traceback na primeira execução.

# Partidas atualizadas e salvas no disco após jogar:

linha: 48 a 50

arquivo: main.py

main.py: Chama salvar_jogadores ao sair no [0], gravando a contagem no jogadores.csv.

# Histórico com múltiplos commits no Git:

linha: Histórico do Git

arquivo: Repositório fliperama no GitHub

GitHub: Múltiplos commits com mensagens descritivas sobre o progresso.

5. Documentação e autoavaliação:
# README.md completo e justificativa da ler_texto:

linha: Arquivo inteiro

arquivo: README.md

README.md: Explica a estrutura do app, autoavaliação e motivo da ler_texto estar em modulos.py (evitar código duplicado).

# Exemplo de execução e revisão do colega:

linha: Seções ## Exemplo de Execução e ## Revisão do Colega

arquivo: README.md

README.md: Exibe a captura do terminal e a avaliação feita pelo colega.

6. Jogo autoral e reúso:
# senhasecreta.py roda no [4] reusando módulos:

linha: Arquivo inteiro (senhasecreta.py) e linha 69 no main.py

arquivo: senhasecreta.py e main.py

main.py: A opção [4] chama o jogo autoral, reusando funções de telas.py e modulos.py.

# Jogo autoral soma 1 no partidas do jogador:

linha: 59 a 64

arquivo: main.py

main.py: Executa incrementar_partida antes de abrir o jogo autoral.

# README-meujogo.md com tabela de reúso e exemplo:

linha: Arquivo inteiro

arquivo: README-meujogo.md

README-meujogo.md: Contém as regras, exemplo de execução e a tabela de reúso nas 4 colunas.