/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1173 - Preenchimento de Vetor 1
 * Autor     : Ian Forbeck
 * LIAC      : Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.
*/
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

void preencher(vector<int> &n, int primeiro) {
    int i;

    n.push_back(primeiro);
    for (i = 1; i < 10; i++) {
        n.push_back(n[i - 1] * 2);
    }
}

void mostrar(vector<int> &n) {
    int i, qtd = n.size();

    for (i = 0; i < qtd; i++) {
        cout << "N[" << i << "] = " << n[i] << endl;
    }
}

int main() {
    vector<int> n;
    int primeiro;

    cin >> primeiro;
    preencher(n, primeiro);
    mostrar(n);
    
    return 0;
}