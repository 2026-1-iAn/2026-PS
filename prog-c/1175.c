/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1175 - Array Change I
* Autor      : Ian Forbeck
* LIAC       : Le 10 intieros num vetor X. Troca os valores menores ou iguais a zero por 1. Imprime cada posicao no formato "X[i] = valor".
*/
#include <stdio.h>

int main() {
    int n[20], i;

    for (i = 0; i < 20; i++) {
        scanf("%d", &n[i]);
    }

    for (i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, n[19 - i]);
    }

    return 0;
}