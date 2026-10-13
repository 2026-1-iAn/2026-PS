/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1179 - Preenchimento de Vetor IV
* Autor      : Ian Forbeck
* LIAC       : Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.
*/
#include <stdio.h>

int main() {
    int entrada[15];
    int par[5];
    int impar[5];
    int qtd_par = 0, qtd_impar = 0;

    for (int i = 0; i < 15; i++) {
        scanf("%d", &entrada[i]);
    }

    for (int i = 0; i < 15; i++) {
        int num = entrada[i];

        if (num % 2 == 0) {
            par[qtd_par] = num;
            qtd_par++;
            
            if (qtd_par == 5) {
                for (int i = 0; i < 5; i++) {
                    printf("par[%d] = %d\n", i, par[i]);
                }
                qtd_par = 0;
            }
        } else {
            impar[qtd_impar] = num;
            qtd_impar++;
            
            if (qtd_impar == 5) {
                for (int i = 0; i < 5; i++) {
                    printf("impar[%d] = %d\n", i, impar[i]);
                }
                qtd_impar = 0;
            }
        }
    }

    for (int i = 0; i < qtd_impar; i++) {
        printf("impar[%d] = %d\n", i, impar[i]);
    }
    
    for (int i = 0; i < qtd_par; i++) {
        printf("par[%d] = %d\n", i, par[i]);
    }

    return 0;
}