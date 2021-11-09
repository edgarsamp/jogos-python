import jogoAdivinhacao
import jogoDaVelha
import jogoForca

def menu_de_jogos():
    print("Opções de jogos:")
    print("1 - Jogo de adivinhação")
    print("2 - Jogo da velha")
    print("3 - Jogo da forca")


    while(True):
        n = int(input("Diga a opção do jogo que deseja jogar: "))

        if n == 1:
            jogoAdivinhacao.jogar()
            break
        elif n == 2:
            jogoDaVelha.jogar()
            break
        elif n == 3:
            jogoForca.jogar()
            break
        else:
            print("Digite uma opção válida")

    




if __name__ == "__main__":
    menu_de_jogos()