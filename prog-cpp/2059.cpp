/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 2059 - Impar, Par ou Roubo
 * Autor     : Ian Forbeck
 * LIAC      : Um novo jogo chamado Ímpar, Par ou Roubo (IPR) está se tornando muito popular. Esse jogo surgiu quando alguns amigos estavam sem conexão com a internet, sem celular, sem computador e bastante desocupados. O jogo está tão popular que irá acontecer um campeonato mundial de IPR e cada país do mundo irá escolher um representante para competir.
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    int p, r1, r2, r, a;
    if (!(cin >> p >> r1 >> r2 >> r >> a)) return 0;

    int soma = r1 + r2;
    bool soma_par = (soma % 2 == 0);

    if (r == 1 && a == 1) {
        cout << "Jogador 2 ganha!\n";
    } else if (r == 1 && a == 0) {
        cout << "Jogador 1 ganha!\n";
    } else if (r == 0 && a == 1) {
        cout << "Jogador 1 ganha!\n";
    } else {
        if ((p == 1 && soma_par) || (p == 0 && !soma_par)) {
            cout << "Jogador 1 ganha!\n";
        } else {
            cout << "Jogador 2 ganha!\n";
        }
    }
    return 0;
}