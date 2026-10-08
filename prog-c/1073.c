/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1073 - Quadrado de Pares
* Autor      : Ian Forbeck
* LIAC       : Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
*/
#include <stdio.h>

int main() {
    int n, i;

    scanf("%d", &n);

    for (i = 2; i <= n; i = i + 2) {
        printf("%d^2 = %d\n", i, i * i);
    }
    
    return 0;
}