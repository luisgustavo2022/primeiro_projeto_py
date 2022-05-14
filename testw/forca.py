def jogar():
    palavra_secreta = ["m", "a", "c", "e", "i", "o"]
    letras_descobertas = []

    print("jogo da forca")

    for i in range(0, len(palavra_secreta)):
        letras_descobertas.append("-")

    acertou = False

    while acertou is False:
        letra = str(input("digite a letra:"))

        for i in range(0, len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                letras_descobertas[i] = letra

            print(letras_descobertas[i])
            acertou = True

        for x in range(0, len(letras_descobertas)):
            if letras_descobertas[x] == "-":
                acertou = False

    print("você acertoou a palavra, parábens")

if __name__ == "__main__":
    jogar()
