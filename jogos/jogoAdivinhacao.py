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
    print("adivinhar")

def adivinhado():
    print("adivinhado")
    

if __name__ == "__main__":
    jogo_de_adivinhacao()