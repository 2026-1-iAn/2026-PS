/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1165 - Numero Primo
* Autor      : Ian Forbeck
* LIAC       : Le N casos. Para cada inteiro X, diz se X eh primo ou nao, no formato "X eh primo" / "X nao eh primo".
*/
#include <stdio.h>

int eh_primo(int n) {
    int i;

    if (n < 2){
        return 0;
    }
    for (i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int casos, k, x;

    scanf("%d", &casos);

    for (k = 0; k < casos; k++) {
        scanf("%d", &x);
        if (eh_primo(x)) {
            printf("%d eh primo\n", x);
        } else {
            printf("%d nao eh primo\n", x);
        }
    }

    return 0;
}