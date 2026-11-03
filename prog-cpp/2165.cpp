/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 2165 - Tuitando
 * Autor     : Ian Forbeck
 * LIAC      : O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.
*/
#include <iostream>
#include <string>
using namespace std;

 int main() {
    string texto;
    getline(cin, texto);
    if (texto.size() <= 140) {
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    } 
    
    return 0;
 }