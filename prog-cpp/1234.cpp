/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1234 - Sentença Dançante
 * Autor     : Ian Forbeck
 * LIAC      : Uma sentença é chamada de dançante se sua primeira letra for maiúscula e cada letra subsequente for o oposto da letra anterior. Espaços devem ser ignorados ao determinar o case (minúsculo/maiúsculo) de uma letra. Por exemplo, "A b Cd" é uma sentença dançante porque a primeira letra ('A') é maiúscula, a próxima letra ('b') é minúscula, a próxima letra ('C') é maiúscula, e a próxima letra ('d') é minúscula.
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    string linha;

    while (getline(cin, linha)) {
        bool maiuscula = true;

        for (char &c : linha) {
            if (isalpha(c)) {
                if (maiuscula) {
                    c = toupper(c);
                } else {
                    c = tolower(c);
                }
                maiuscula = !maiuscula;
            }
        }

        cout << linha << "\n";
    }
    return 0;
}