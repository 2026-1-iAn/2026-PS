/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1114 - Senha Fixa
* Autor      : Ian Forbeck
* LIAC       : Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.
*/
#include <stdio.h>

int main() {
    int senha;

    scanf("%d", &senha);

    while (senha != 2002) {
        printf("Senha Invalida\n");
        scanf("%d", &senha);
    }

    printf("Acesso Permitido\n");

    return 0;
}