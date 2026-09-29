/*
Problema 1011 BeeCrowd
2026.09.22
Ian Forbeck
*/

#include <stdio.h>

int main(){
    double r=0, v=0;
    scanf("%lf", &r);
    v = (4.0/3.0)*3.14159*(r*r*r);
    printf("VOLUME = %.3lf\n", v);
    return 0;
}