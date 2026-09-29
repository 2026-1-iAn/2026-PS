/*
Problema 1043 BeeCrowd
2026.09.29
Ian Forbeck
*/

#include <stdio.h>

int main(){
    float a, b, c;

    scanf("%f %f %f", &a, &b, &c);

    if (a < b + c && b < a + c && c < a + b) {
        printf("Perimetro = %.1lf\n", a + b + c);
    } else {
        printf("Area = %.1f\n", (a + b) * c / 2);
    }
    return 0;
}