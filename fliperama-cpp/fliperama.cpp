/*
- Disciplina: 2026-PCAP
- Projeto   : MeuApp v4.0 - o Fliperama em C++ (Aula 32)
- Autor     : Ian Forbeck
- LIAC      : Menu com validacao, cadastro, exclusao e listagem de jogadores em dois vectors que crescem, um jogo que conta partidas por jogador e o cadastro salvo em arquivo apos cada alteracao e relido na entrada.
*/
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <ctime>
using namespace std;

#define DONO "IAN FORBECK"
#define ARQUIVO "jogadores.csv"

void linha() {
    cout << "============================================" << endl;
}

void titulo(string texto) {
    linha();
    cout << "    " << texto << endl;
    linha();
}

int ler_numero(string mensagem, int minimo, int maximo) {
    int numero;

    cout << mensagem << ": ";
    cin >> numero;
    while (cin.fail() || numero < minimo || numero > maximo) {
        if (cin.fail()) {
            cin.clear();                // destrava o cin, que parou no que nao era numero
            cin.ignore(1000, '\n');     // e joga fora o resto da linha
        }
        cout << "Opcao invalida! Tente de novo: ";
        cin >> numero;
    }
    return numero;
}

string ler_texto(string mensagem) {
    string texto;

    cout << mensagem << ": ";
    cin >> texto;   // uma palavra, sem espaços
    return texto;
}

int buscar(vector<string> &apelidos, string procurado) {
    int i, qtd = apelidos.size();

    for (i = 0; i < qtd; i++) {
        if (apelidos[i] == procurado) {
            return i;
        }
    }
    return -1;
}

void salvar(vector<string> &apelidos, vector<int> &partidas) {
    ofstream arquivo(ARQUIVO);
    int i, qtd = apelidos.size();

    for (i = 0; i < qtd; i++) {
        arquivo << apelidos[i] << "," << partidas[i] << endl;
    }
}

void carregar(vector<string> &apelidos, vector<int> &partidas) {
    ifstream arquivo(ARQUIVO);
    string apelido;
    int n;

    while (getline(arquivo, apelido, ',')) {    // le ate a virgula
        arquivo >> n;                           // o numero de partidas
        arquivo.ignore();                       // o Enter que sobrou
        apelidos.push_back(apelido);
        partidas.push_back(n);
    }
}

void cadastrar(vector<string> &apelidos, vector<int> &partidas) {
    string novo;

    titulo("NOVO JOGADOR");
    novo = ler_texto("Apelido (sem espaços)");

    if (buscar(apelidos, novo) != -1) {
        cout << "Esse apelido ja esta cadastrado!" << endl;
        return;
    }

    apelidos.push_back(novo);
    partidas.push_back(0);
    salvar(apelidos, partidas);
    cout << "Jogador " << novo << " cadastrado." << endl;
}

void excluir(vector<string> &apelidos, vector<int> &partidas) {
    string quem;
    int pos;

    titulo("EXCLUIR JOGADOR");
    quem = ler_texto("Apelido para excluir");
    pos = buscar(apelidos, quem);
    if (pos == -1) {
        cout << "Jogador nao encontrado." << endl;
        return;
    }

    apelidos.erase(apelidos.begin() + pos);
    partidas.erase(partidas.begin() + pos);
    salvar(apelidos, partidas);
    cout << "Jogador " << quem << " excluido." << endl;
}

void listar(vector<string> &apelidos, vector<int> &partidas) {
    int i, qtd = apelidos.size();

    titulo("JOGADORES CADASTRADOS");
    if (qtd == 0) {
        cout << "Nenhum jogador cadastrado ainda." << endl;
    }
    for (i = 0; i < qtd; i++) {
        cout << apelidos[i] << " | " << partidas[i] << " partidas" << endl;
    }
}

void jogar_adivinhe(vector<string> &apelidos, vector<int> &partidas) {
    string quem;
    int pos, segredo, palpite, tentativas;

    titulo("ADIVINHE O NUMERO");
    quem = ler_texto("Quem vai jogar");
    pos = buscar(apelidos, quem);
    if (pos == -1) {
        cout << "Cadastre esse apelido antes de jogar." << endl;
        return;
    }

    segredo = rand() % 100 + 1;
    cout << "Pensei num numero de 1 a 100." << endl;

    palpite = ler_numero("Seu palpite", 1, 100);
    tentativas = 1;
    while (palpite != segredo) {
        if (palpite < segredo) {
            cout << "Maior!" << endl;
        } else {
            cout << "Menor!" << endl;
        }
        palpite = ler_numero("Seu palpite", 1, 100);
        tentativas = tentativas + 1;
    }
    cout << "Acertou em " << tentativas << " tentativas, " << quem << "!" << endl;

    partidas[pos] = partidas[pos] + 1; // a partida so conta quando o jogo termina
    salvar(apelidos, partidas);
}

void mostrar_menu() {
    linha();
    cout << "   FLIPERAMA DO " << DONO << endl;
    linha();
    cout << "[1] Adivinhe o Numero" << endl;
    cout << "[2] Cadastrar jogador" << endl;
    cout << "[3] Listar jogadores" << endl;
    cout << "[4] Excluir jogador" << endl;
    cout << "[0] Sair" << endl;
    linha();
}

int main() {
    vector<string> apelidos;
    vector<int> partidas;
    int opcao;

    srand(time(NULL));
    carregar(apelidos, partidas);

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 4);
    while (opcao != 0) {
        if (opcao == 1) {
            jogar_adivinhe(apelidos, partidas);
        } else if (opcao == 2) {
            cadastrar(apelidos, partidas);
        } else if (opcao == 3) {
            listar(apelidos, partidas);
        } else {
            excluir(apelidos, partidas);
        }
        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 4);
    }

    salvar(apelidos, partidas);
    titulo("Ate a proxima!");
    return 0;
}