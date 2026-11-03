/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1011 - Esfera
 * Autor     : Ian Forbeck
 * LIAC      : Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int r;
    double volume;

    cin >> r;
    volume = (4 / 3.0) * 3.14159 * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;
    
    return 0;
}