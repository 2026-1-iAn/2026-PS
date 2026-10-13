/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1153 - Fatorial Simples
* Autor      : Ian Forbeck
* LIAC       : Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
*/
#include <stdio.h>

int main() {
    int N, i;
    int fatorial = 1;

    scanf("%d", &N);

    for (i = 1; i <= N; i++) {
        fatorial *= i;
    }

    printf("%d\n", fatorial);
    return 0;
}