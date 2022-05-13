import random

print('bem vindo o o jogo de advinhação')

n_s = round(random.randrange(1, 100))
print('qula o nivem de dificuldade?')
print('(1)fácil  (2)médio  (3)difícil')
nivel = int(input('defina o nível:'))

facil = nivel == 1
medio = nivel == 2
dificil = nivel == 3
chance = 1000
score = 0
if facil:
    chance = 20
elif medio:
    chance = 10
else:
    chance = 5

while chance > 0:
    chutestr = input('Adivinhe o número entre 1 e 100: ')
    chute = int(chutestr)
    acertou = chute == n_s
    maior = chute > n_s
    menor = chute < n_s
    if chute < 1 or chute > 100:
        print("coloque um número entre 1 e 100")
        continue
    elif acertou:
        print("você acertou")
        chance = 0
        print("você fez {} de pontuação.".format(score))
    else:
        if maior:
            print("você errou!, o número é menor.")
            chance = chance - 1
            print("você tem mais {} chances".format(chance))
        elif menor:
            print("você errou!, o número é maior.")
            print("você tem mais {} chances".format(chance))
    chance = chance - 1
    perdidos = abs(chute - n_s)
    score = score - perdidos

print("o número era ", n_s)
print("fim do jogo")
