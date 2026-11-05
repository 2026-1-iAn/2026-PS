/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1174 - Seleção em Vetor 1
 * Autor     : Ian Forbeck
 * LIAC      : Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.
*/
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    vector<double> a;
    double x;
    int i, qtd;

    for (i = 0; i < 100; i++) {
        cin >> x;
        a.push_back(x);
    }

    qtd = a.size();
    cout << fixed << setprecision(1);
    for ( i = 0; i < qtd; i++) {
        if (a[i] <= 10) {
            cout << "A[" << i <<"] = " << a[i] << endl;
        }
    }
    
    return 0;
}