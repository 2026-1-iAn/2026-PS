/*
Problema 1043 BeeCrowd
2026.09.29
Ian Forbeck
*/

#include <stdio.h>
// linha que esta o for apaga o ; depois do parenteses
int main(){
    int n, i;

    scanf("%d", &n);

    for (i = 1; i <= 10; i++)
    {
        printf("%d x %d = %d\n", i, n, i * n);
    }
    
    return 0;
}