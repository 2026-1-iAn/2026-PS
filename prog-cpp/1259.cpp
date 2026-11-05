/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1259 - Pares e Impares
 * Autor     : Ian Forbeck
 * LIAC      : Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério: Primeiro os Pares depois os Ímpares sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.
*/
#include <iostream>
#include <vector>
#include <iomanip>
#include <functional>
using namespace std;

void mostrar(vector<int> &v) {
    int i, qtd = v.size();

    for (i = 0; i < qtd; i++) {
        cout << v[i] << endl;
    }
}

int main() {
    vector<int> pares, impares;
    int n, x, i;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> x;
        if (x % 2 == 0) {
            pares.push_back(x);
        } else {
            impares.push_back(x);
        }
    }

    sort(pares.begin(), pares.end());
    sort(impares.begin(), impares.end(), greater<int>());

    mostrar(pares);
    mostrar(impares);

    return 0;
}