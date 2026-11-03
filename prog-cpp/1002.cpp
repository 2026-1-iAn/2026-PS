/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1002 - Área do Círculo
 * Autor     : Ian Forbeck
 * LIAC      : A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159: - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;

    cin >> r;
    area = 3.14159 * r * r;
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}