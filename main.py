print('bem vindo o o jogo de advinhação')

n_s = 43
chutestr = input('adivinhe o número: ')
chute = int(chutestr)
acertou = chute == n_s
maior = chute > n_s
menor = chute < n_s
if acertou:
    print("você acertou")
else:
    if maior :
        print("você errou!, o número é menor.")
    elif menor :
        print("você errou!, o número é maior.")

print("fim do jogo")
