/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1175 - Array Change I
* Autor      : Ian Forbeck
* LIAC       : Le um inteiro para N[0]. Cada posicao seguinte vale o dobro da anterior, ate N[9]. Imprime as 10 posicoes "N[i] = valor".
*/
#include <stdio.h>

int main() {
    int n[10], i;

    scanf("%d", &n[0]);

    for (i = 1; i < 10; i++) {
        n[i] = n[i - 1] * 2;
    }

    for (i = 0; i < 10; i++) {
        printf("N[%d] = %d\n", i, n[i]);
    }

    return 0;
}