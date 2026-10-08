/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1067 - Números Ímpares
* Autor      : Ian Forbeck
* LIAC       : Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
*/
#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x);

    for (int i = 1; i <= x; i++) {
        if (i % 2 != 0) {
            printf("%d\n", i);
        }
    }
    return 0;
}