from os import sep
import random

def jogar():
    print("Jogo da forca")
    tentativas = set()
    ganhou = False
    qnt_erros = 0
    palavra = gera_palavra()
    palavra_oculta = ["_" for letra in palavra]

    while(qnt_erros < 7):
        desenha_forca(qnt_erros)
        print("Fruta: ", *palavra_oculta, sep="")
        print("Letras tentadas:", *tentativas)
        tentativa = ""
        while(True):
            tentativa = input("Diga uma letra: ").lower()
            if(tentativa in tentativas):
                print("Voce ja tentou essa letra")
            else:
                break

        tentativas.add(tentativa)
        
        if(tentativa in palavra):
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    palavra_oculta[i] = tentativa
        else:
            qnt_erros += 1
        if palavra_oculta == list(palavra):
            ganhou = True
            break
    
    if(ganhou):
        print("Parabens voce acertou a palavra")
    else:
        print("Voce nao conseguiu acertar a palavra")
        

def gera_palavra():
    arq = open("palavras.txt", "r")
    palavras = []
    for palavra in arq:
        palavras.append(palavra.strip())
    return palavras[random.randrange(0, len(palavras))]

def desenha_forca(qnt_erros):
    print("  _______     ")
    print(" |/      |    ")

    if(qnt_erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")
    if(qnt_erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(qnt_erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(qnt_erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(qnt_erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(qnt_erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (qnt_erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         \n")



if __name__ == "__main__":
    jogar()