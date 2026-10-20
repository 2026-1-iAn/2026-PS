/*
Disciplina: 2026-PCAP
Projeto   : MeuApp v3.0 - o Fliperama em C (Aula 28)
Autor     : Ian Forbeck
LIAC      : Menu com validacao, cadastro de jogadoresem vetores com contagem, um jogo que conta partidas por jogador e o cadastro salvo em arquivo na saida e relido na entrada.
*/
#include <stdio.h>

#define DONO "IAN FORBECK"

void linha() {
    printf("************************************************\n");
}

void titulo(char texto[]) {
    linha();
    printf("    %s\n", texto);
    linha();
}

int ler_numero(char mensagem[], int minimo, int maximo) {
    int numero, lidos;

    printf("%s: ", mensagem);
    lidos = scanf("%d", &numero);
    while (lidos !=1 || numero < minimo || numero > maximo) {
        if (lidos != 1) {
            scanf("%*s"); /* joga fora o que nao era numero */
        }
        printf("Opção inválida! Tente de novo: ");
        lidos = scanf("%d", &numero);
    }
    return numero;
}

void mostrar_menu() {
    linha();
    printf("FLIPERAMA DO %s\n", DONO);
    linha();
    printf("[1] Adivinhe o número\n");
    printf("[2] Cadastrar jogador\n");
    printf("[3] Listar jogadores\n");
    printf("[0]Sair\n");
    linha();
}

int main() {
    int opcao;

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 3);
    while (opcao != 0) {
        if (opcao == 1) {
            printf("O jogo entra na Fase 3.\n");
        } else if (opcao == 2) {
            printf("O cadastro entra na Fase 2.\n");
        } else if (opcao == 1) {
            printf("A lista entra na Fase 2.\n");
        }
        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 3);
    }

    titulo("Ate a proxima!");
    return 0;
}