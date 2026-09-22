/* Comentário de Bloco
Programa: Hello.c
Data: 2026.09.22
Autor: Ian Forbeck
*/

// importa biblioteca padrão de entrada e saida
#include <stdio.h>

// defino a função principal do tipo int
int main(){
    // printf == Saída --> Mostra na Tela
    // "entre aspas == texto"
    // comando se encerra com ;
    printf("Hello World!\n");

    // Receber 2 valores somar e mostrar o resultado
    
    int num1=0, num2=0;
    printf("Digite um numero: ");
    scanf("%d", &num1);
    printf("Digite outro numero: ");
    scanf("%d", &num2);
    int soma = num1+num2;
    printf("Soma: %d\n", soma);

    // indica que chegou ao fim da função
    return 0;
}

/*
para compilar ==
gcc <nome-do-arquivo> -o nome-do-programa

para executar ==
./nome-do-programa
*/