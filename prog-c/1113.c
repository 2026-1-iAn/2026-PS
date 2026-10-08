/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1113 - Crescente e Decrescente
* Autor      : Ian Forbeck
* LIAC       : Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
*/
#include <stdio.h>

int main() {
    int x, y;

    scanf("%d %d", &x, &y);

    while (x != y) {
        if (x < y) {
            printf("Crescente\n");
        } else {
            printf("Decrescente\n");
        }
        scanf("%d %d", &x, &y);
    }

    return 0;
}