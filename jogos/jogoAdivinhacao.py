import random

def jogo_de_adivinhacao():
    print("Jogo de adivinhacao")
    while(True):
        opcao = int(input('1 - Adivinhar um numero\n2 - Ter um numero adivinhado\n'))
        if(opcao == 1 or opcao == 2):
            break
    if opcao == 1:
        adivinhar()
    else:
        adivinhado()

def adivinhar():
    chances = 5
    tentativas = []

    numero = random.randrange(20)
    print("Foi sorteado aleatoriamente um numero entre 0 e 20")
    print(f"Voce tem {chances} chances")
    while(chances > 0):
        n = int(input("De seu chute: "))
        chances -=1

        if n == numero:
            break

        print("Nao acertou")
        tentativas.append(n)
        print("numeros tentados: ", end="")
        print(*tentativas)

    if chances == 0:
        print("Voce nao conseguiu adivinhar o numero :(")
    else:
        print("Parabens voce conseguiu adivinhar o numero e ainda sobraram", chances, "tentativas!")

def adivinhado():
    print("adivinhado")


if __name__ == "__main__":
    jogo_de_adivinhacao()