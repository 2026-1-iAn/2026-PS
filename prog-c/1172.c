/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1172 - Array Replacemenet I
* Autor      : Ian Forbeck
* LIAC       : Le 10 intieros num vetor X. Troca os valores menores ou iguais a zero por 1. Imprime cada posicao no formato "X[i] = valor".
*/
#include <stdio.h>

int main() {
    int x[10], i;

    for (i = 0; i < 10; i++) {
        scanf("%d", &x[i]);
        if (x[i] <= 0) {
            x[i] = 1;
        }
    }

    for (i = 0; i < 10; i++) {
        printf("X[%d] = %d\n", i, x[i]);
    }

    return 0;
}