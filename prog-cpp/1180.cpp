/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1168 - LED
 * Autor     : Ian Forbeck
 * LIAC      : Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.
*/
#include <iostream>
#include <vector>
using namespace std;

int posicao_do_menor(vector<int> &v) {
    int i, pos = 0, qtd = v.size();

    for (i = 1; i < qtd; i++) {
        if (v[i] < v[pos]) {
            pos = i;
        }
    }
    return pos;
}

int main() {
    vector<int> v;
    int n, x, i, pos;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }

    pos = posicao_do_menor(v);

    cout << "Menor valor: " << v[pos] << endl;
    cout << "Posicao: " << pos << endl;

    return 0;
}