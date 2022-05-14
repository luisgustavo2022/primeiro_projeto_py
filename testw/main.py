import forca
import advinhacao

def escolha():
    print('escolha o seu jogo')
    print('(1) forca  (2) adivinhação')

    escolha = int(input('qual jogo?'))

    if escolha == 1:
        forca.jogar()
    elif escolha == 2:
        advinhacao.jogar()
    else:
        print('erro')
if __name__ == "__main__":
    escolha()