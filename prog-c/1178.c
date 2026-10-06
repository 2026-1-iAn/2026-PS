/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1178 - Array Change I
* Autor      : Ian Forbeck
* LIAC       : Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.
*/
#include <stdio.h>

int main() {
    double n[100];
    int i;

    scanf("%lf", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %.4lf\n", i, n[i]);
    }

    return 0;
}