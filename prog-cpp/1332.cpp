/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1332 - Um-Dois-Três
 * Autor     : Ian Forbeck
 * LIAC      : Seu irmão mais novo aprendeu a escrever apenas um, dois e três, em Inglês. Ele escreveu muitas dessas palavras em um papel e a sua tarefa é reconhecê-las. Nota-se que o seu irmão mais novo é apenas uma criança, então ele pode fazer pequenos erros: para cada palavra, pode haver, no máximo, uma letra errada. O comprimento de palavra é sempre correto. É garantido que cada palavra que ele escreveu é em letras minúsculas, e cada palavra que ele escreveu tem uma interpretação única.
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, i;
    string s;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> s;
        if (s.size() == 5) {
            cout << 3 << endl;
        } else if ((s[0] == 'o' && s[1] == 'n') || (s[0] == 'o' && s[2] == 'e') || (s[1] == 'n' && s[2] == 'e')) {
            cout << 1 << endl;
        } else {
            cout << 2 << endl;
        }
    }

    return 0;
}