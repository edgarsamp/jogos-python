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

    numero = random.randrange(1, 20)
    print("Foi sorteado aleatoriamente um numero entre 1 e 20")
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
    print("Escolha um numero de 1 a 20, o programa tentara adivinhar e voce deve respoder com:")
    print("maior   - caso o chute do computador for menor que seu numero")
    print("maior   - caso o chute do computador for menor que seu numero")
    print("acertou - caso o chute do computador estiver certo")

    #Busca binaria
    l = 1
    r = 20
    tentativas = 0

    while(r > l+1):
        tentativas += 1
        chute = (l+r)//2
        check = input(f"Chute: {chute} -> ")
        if(check.lower() == "acertou"):
            break
        if(check.lower() == "maior"):
            l = chute
        elif(check.lower() == "menor"):
            r = chute
        else:
            print("Entrada invalida")
            tentativas -= 1
        
    print(f"O computador precisou de {tentativas} para acertar seu numero")

if __name__ == "__main__":
    jogo_de_adivinhacao()