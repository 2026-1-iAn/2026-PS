# Conserto 4: trecho do "Pedra-Papel-Tesoura" (Aula 17)
jogada = input("pedra, papel ou tesoura? ").lower()

if jogada == "pedra" or jogada == "papel" or jogada == "tesoura":
    print("Jogada valida:", jogada)
else:
    print("Jogada invalida!")