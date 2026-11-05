/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1551 - Frase Completa
 * Autor     : Ian Forbeck
 * LIAC      : Seu professor de português não para de trazer coisas novas para a sala, e hoje não foi diferente. Existe uma cidade, segundo seu professor, onde as pessoas levam muito a sério a forma como elas se comunicam. Em especial, quando duas pessoas estão conversando, elas pensam muito nas frases antes de dizê-las, de forma a garantir que tal frase seja uma “frase completa”, ou talvez uma “frase quase completa”. Considerando o nosso alfabeto de 26 letras, uma frase é dita “completa” quando ela contém todas as letras do alfabeto contidas nela. De modo semelhante, uma frase é dita “quase completa” se ela não é completa, porém contém ao menos metade das letras do alfabeto contidas nela. Quando uma frase não é “completa” e nem “quase completa”, ela é dita “mal elaborada”. Seu professor lhe deu uma tarefa muito difícil: dadas várias frases trocadas entre vários habitantes da cidade citada, diga em qual das categorias acima a frase se encaixa.
*/
#include <iostream>
#include <string>
using namespace std;

int conta_letras(string frase) {
    int total = 0, i, tam = frase.size();
    char letra;
    bool achou;
    for (letra = 'a'; letra <= 'z'; letra++) {
        achou = false;
        for (i = 0; i < tam; i++) {
            if (frase[i] == letra) {
                achou = true;
            }
        }
        if (achou) {
            total++;
        }
    }
    return total;
}
int main() {
    int n, i, letras;
    string frase;
    cin >> n;
    cin.ignore();
    for (i = 0; i < n; i++) {
        getline(cin, frase);
        letras = conta_letras(frase);
        if (letras == 26) {
            cout << "frase completa" << endl;
        } else if (letras >= 13) {
            cout << "frase quase completa" << endl;
        } else {
            cout << "frase mal elaborada" << endl;
        }
    }
    return 0;
}