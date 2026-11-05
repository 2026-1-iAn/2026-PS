/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1178 - Preenchimento de Vetor 3
 * Autor     : Ian Forbeck
 * LIAC      : Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.
*/
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

void preencher(vector<double> &n, double primeiro) {
    int i;

    n.push_back(primeiro);
    for (i = 1; i < 100; i++) {
        n.push_back(n[i - 1] / 2);
    }
}

void mostrar(vector<double> &n) {
    int i, qtd = n.size();

    cout << fixed << setprecision(4);
    for (i = 0; i < qtd; i++) {
        cout<< "N[" << i << "] = " << n[i] << endl;
    }
}

int main() {
    vector<double> n;
    double primeiro;

    cin >> primeiro;
    preencher(n, primeiro);
    mostrar(n);
    
    return 0;
}