# Fliperama em C++ (MeuApp v4.0)


## O que e
Um aplicativo de terminal que gerencia o cadastro de jogadores (cadastrar, listar e excluir), contabiliza partidas no jogo "Adivinhe o Número" e salva os dados em disco.
É a evolução da versão v3.0 em C (Aula 28), refatorada para C++ na Aula 32 de 2026-PCAP.


## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama


## Arquivos
- fliperama.cpp: Código-fonte principal com o menu validado, cadastro dinâmico de jogadores, jogo e manipulação de arquivos.
- jogadores.csv: Guarda os dados persistidos, contendo o apelido (texto) e o total de partidas (inteiro) separados por vírgula.


## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 70) | apelidos.push_back(novo) (l. 94) |
| comparar apelidos | strcmp(...) == 0 (l. 47) | == (l. 54) |
| a funcao que cadastra | int cadastrar(..., int qtd) (l. 54) | void cadastrar(... &apelidos, ...) (l. 83) |
| manipular arquivos | FILE *arquivo = fopen(...) e fclose() (l. 113, 120) | ofstream / ifstream com fechamento automático (l. 61, 71) |
| cadastro cheio | if (qtd >= CAPACIDADE) (l. 59) | Não existe (o std::vector cresce sob demanda) |
| excluir um jogador | Não existia na v3.0 | apelidos.erase(apelidos.begin() + pos) (l. 111) |

A função `cadastrar` deixou de devolver `int` porque o `std::vector` é passado por referência (`&`) e gerencia seu próprio tamanho via `.size()`.
Com isso, não é mais necessário retornar o contador `qtd` atualizado para o `main`.


## O que o C++ decidiu por mim
O `std::vector` gerencia a alocação e o redimensionamento da memória automaticamente, eliminando o limite fixo `CAPACIDADE` e o contador manual `qtd` do C.
Além disso, os fluxos `ifstream` e `ofstream` fecham os arquivos sozinhos ao saírem do escopo, dispensando o `fclose()`.


## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | B | `fliperama.cpp` (l. 1–6, l. 176–177) e 6+ commits no Git |
| 2. Cadastro: vectors e referencia | B | `fliperama.cpp` (l. 50, 83, 89–92, 100–115) |
| 3. Jogo e partidas | B | `fliperama.cpp` (l. 136–139, 158, 160–161) |
| 4. Persistencia | B | `fliperama.cpp` (l. 71–81, 96, 113, 199) e `jogadores.csv` |
| 5. Documentacao e comparacao | B | `README.md` (6 seções, tabela de 6 linhas e explicação do `void`) |