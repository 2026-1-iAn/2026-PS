# Senha Secreta (senhasecreta.py)

## Regras do Jogo
O computador sorteia uma senha contendo 3 números únicos (de 0 a 9). O jogador possui 10 tentativas para acertar a sequência exata. A cada tentativa, o programa fornece o retorno das posições:
- **Na posição certa:** Quantidade de números corretos e na posição exata.
- **Apenas existe na senha:** Quantidade de números que pertencem à senha, mas estão em posições incorretas.

## Tabela de Reúso de Módulos
| Função Reutilizada | Módulo de Origem | Finalidade no Jogo |

| `titulo()`         | `telas.py`       | Exibição do cabeçalho do jogo e telas de resultado |
| `linha()`          | `telas.py`       | Divisão visual entre as rodadas e dicas |
| `ler_texto()`      | `modulos.py`     | Leitura e validação da entrada dos números sem aceitar valores vazios |