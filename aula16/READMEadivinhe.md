# Entrada:
1 - 'palpite = int(*input*("Seu palpite (1 a " + str(maximo) + "): "))' linha 16; 
2 - 'opcao = int(*input*("Digite 1, 2 ou 3: "))' linha 43; 
3 - ''

# Saída:
1 - '*print*("1 - Fácil       (1 a 10, 3 chances)")' linha 40;
2 - '*print*("2 - Médio       (1 a 100, 5 chances)")' linha 41; 
3 - '*print*("3 - Impossível  (1 a 1000, 10 chances)")' linha 42;

# Operadores:
1 - 'while chances *>* 0 and not acertou:' linha 15; 
2 - ' if palpite *==* numero_secreto:' linha 18;
3 - 'palpite = int(input("Seu palpite (1 a " *+* str(maximo) + "): "))' linha 16

# Sub-rotinas:
1 - '*def* jogar(maximo, chances):' linha 11 a 29 '*return* acertou'
2 - ''
3 - ''

# Condição:
1 - '*if* palpite == numero_secreto:' linha 18;
2 - '*else*:' linha 23;
3 - '*elif* palpite < numero_secreto:' linha 21;

# Repetição:
1 - '*while* chances > 0 and not acertou:' linha 15;
2 - ''
3 - ''

# Variáveis:
1 - '*opcao* = int(input("Digite 1, 2 ou 3: "))' linha 43;
2 - '*nivel* = niveis[opcao - 1]' linha 46;
3 - '*venceu* = jogar(nivel[1], nivel[2])' linha 50.