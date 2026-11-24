/*
 * Disciplina: 2026-PCAP
 * Projeto   : MeuApp v5.0 - o Fliperama em Java (Aula 33)
 * Autor     : Ian Forbeck
 * LIAC      : O primeiro programa em Java: uma classe, o main e uma linha na tela, para provar que o ambiente funciona.
 */
import java.util.Scanner;

public class Fliperama {
    static final String DONO = "IAN FORBECK";
    static Scanner teclado = new Scanner(System.in);

    static void linha() {
        System.out.println("------------------------------------");
    }

    static void titulo(String texto) {
        linha();
        System.out.println("  " + texto);
        linha();
    }

    static int lerInteiro() {
        int numero = -1;            // -1 quer dizer: nao era numero

        if (teclado.hasNextInt()) { // o que vem ai e um numero inteiro?
            numero = teclado.nextInt();
        }
        teclado.nextLine();         // joga fora o resto da linha, com o Enter
        return numero;
    }

    static int lerNumero(String mensagem, int minimo, int maximo) {
        int numero;

        System.out.print(mensagem + ": ");
        numero = lerInteiro();
        while (numero < minimo || numero > maximo) {
            System.out.print("Opcao invalida! Tente de novo: ");
            numero = lerInteiro();
        }
        return numero;
    }

    static void mostrarMenu() {
        linha();
        System.out.println("  FLIPERAMA DO " + DONO);
        linha();
        System.out.println("[1] Adivinhe o Numero");
        System.out.println("[2] Cadastrar jogador");
        System.out.println("[3] Listar jogadores");
        System.out.println("[0] Sair");
        linha();
    }

    public static void main(String[] args) {
        int opcao;

        mostrarMenu();
        opcao = lerNumero("Sua escolha", 0, 3);
        while (opcao != 0) {
            if (opcao == 1) {
                System.out.println("O jogo entra na Fase 3.");
            } else if (opcao == 2) {
                System.out.println("O cadastro entra na Fase 2.");
            } else {
                System.out.println("A lista entra na Fase 2.");
            }
            mostrarMenu();
            opcao = lerNumero("Sua escolha", 0, 3);
        }

        titulo("Ate a proxima!");
    }
}