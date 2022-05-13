print('bem vindo o o jogo de advinhação')

n_s = 43
chutestr = input('adivinhe o número: ')
chute = int(chutestr)
if n_s == chute:
    print("você acertou")
else :
    print("você errou!")

print("fim do jogo")
