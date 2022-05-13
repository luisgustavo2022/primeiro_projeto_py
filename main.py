print('bem vindo o o jogo de advinhação')

n_s = 43
chances = 3

while chances > 0:
    chutestr = input('adivinhe o número: ')
    chute = int(chutestr)
    acertou = chute == n_s
    maior = chute > n_s
    menor = chute < n_s
    if acertou:
        print("você acertou")
        chances = 0
    else:
        if maior:
            print("você errou!, o número é menor.")
            chances = chances - 1
        elif menor:
            print("você errou!, o número é maior.")
            chances = chances - 1




    print("fim do jogo")
