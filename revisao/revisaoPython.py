### Fundamentos de Programação

## 1. Variáveis e tipos de dados
# Váriaveis são códigos usados para armazenar dados na memória do computador, esses dados podem ser consultados e alterados futuramente no código. Toda variável tem um nome
# Temos ao todo 4 tipos de dados, sendo string para textos, int para inteiros, float para decimais e bool para True ou False
# Exemplo:

nome = 'ian' # nome é a variável do tipo string (usada para textos) 

## 2. Operadores
# São símbolos usados para realizar contas, podendo incluir não só números como váriaveis. Também temos 4 tipos de operadores, sendo eles Atribuição, Aritméticos, Relacionais e Lógicos
# Alguns operadores aritméticos são: +, -, ==, /, //, %, **, sendo respectivamente adição, subtração, igual, divisão, divisão inteira, resto e potênciação.
# Exemplo: 

x = 5 + 8 # o operador é '+', representando um operador aritmético e uma adição entre os números 5 e 8. A váriavel x recebe o resultado dessa soma

## 3. Entrada de dados
# É quando o usuário se comunica com o computador 
# Exemplo: 

nome = input("Nome: ") # a entrada é 'input'

## 4. Saida de dados
# É quando o computador se comunica com o usuário
# Exemplo:

print("Hello World!") # a saida é 'print'

## 5. Estrutura de Repetição
# Permitem que ocorra um loop, que o código se repita
# Temos 2 tipos de estrutura de repetição, são eles: 'for' e 'while', usamos 'for' quando sabemos por quantas vezes precisamos repetir o código, enquanto o 'while' é usado para repetir até algo mudar. Além disso, usamos o código 'range' para indicar quantas vezes deve se repetir, ou seja, o alcance
# Exemplo:

for i in range (5): # a repetição é 'range'
    print("Olá!")

## 6. Estrutura de Condição
# Permitem que o programa 'tome decisões', ou seja, executar um código apenas se um condição for 'True'
# Os códigos mais usados para condição são: 'if, 'else' e 'elif'. Sempre deve conter ':' no fim
# Exemplo:

if x + 7 == 20: # a condição é 'if'
    print("A soma está correta")

## Junção dos fundamentos:

while True:  # Repetição = while

    nome = input("Seu nome: ")          # Variável = nome | Entrada = input
    idade = int(input("Sua idade: "))   # Variável = idade | Entrada = input

    print("Olá,", nome, ", você tem", idade, "anos")  # Saída = print

    if idade >= 18:  # Condição = if | Operador = >=
        print("Você é maior de idade")  # Saída = print
    else:  # Condição = else
        print("Você é menor de idade")  # Saída = print

    resposta = input("Deseja cadastrar outra pessoa? (s/n): ")  # Variável = resposta | Entrada = input

    if resposta != "s":  # Condição = if | Operador = !=
        print("Programa encerrado.")  # Saída = print
        break  # Repetição = encerra o while