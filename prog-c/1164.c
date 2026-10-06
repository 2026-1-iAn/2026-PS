/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1164 - Numero Perfeito
* Autor      : Ian Forbeck
* LIAC       : Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.
*/
#include <stdio.h>

int eh_perfeito(int n) {
    int i, soma = 0;

    for (i = 1; i < n; i++) {
        if (n % i == 0) {
            soma = soma + i;
        }
    }
    return soma == n;
}

int main() {
    int casos, k, x;

    scanf("%d", &casos);

    for (k = 0; k < casos; k++) {
        scanf("%d", &x);
        if (eh_perfeito(x)) {
            printf("%d eh perfeito\n", x);
        } else {
            printf("%d nao eh perfeito\n", x);
        }
    }

    return 0;
}