/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1168 - LED
 * Autor     : Ian Forbeck
 * LIAC      : João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    int leds_por_digito[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    while (n--) {
        string numero;
        cin >> numero;

        long long total_leds = 0;

        for (char c : numero) {
            int digito = c - '0';
            total_leds += leds_por_digito[digito];
        }

        cout << total_leds << " leds\n";
    }
    return 0;
}