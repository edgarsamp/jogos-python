def jogar():
    tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]

    imprime_tabuleiro(tabuleiro)

    jogador_da_vez = 1
    jogadas = 0

    while(not check_status_jogo(tabuleiro)):
        jogadas +=1
        jogador_da_vez += 1
        jogador_da_vez %= 2

        while(True): # Enquanto nao for uma jogada valida
            jogada = input("jogador " + str(1+jogador_da_vez%2)+ " é a sua vez ")
            if(joga(jogada, jogador_da_vez, tabuleiro)):
                break
            else:
                print("Jogada inválida!")
        if(jogadas == 9):
            break
        imprime_tabuleiro(tabuleiro)
    
    if(check_status_jogo(tabuleiro)):
        print("jogador", str(1+jogador_da_vez%2), "ganhou!!")
    elif(jogadas == 9):
        print("Deu velha")

def check_status_jogo(tabuleiro):
    # Checa se algum jogador alinhou 3 em uma linha
    if (abs(sum(tabuleiro[0])) == 3 or abs(sum(tabuleiro[1])) == 3 or abs(sum(tabuleiro[2])) == 3):
        return True

    # Checa se algum jogador alinhou 3 em uma linha
    for i in range(3):
        soma = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if abs(soma) == 3:
            return True 

    #diagonal principal
    soma = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    if abs(soma) == 3:
        return True 

    #diagonal secundaria
    soma = tabuleiro[2][0] + tabuleiro[1][1] + tabuleiro[0][2]
    if abs(soma) == 3:
        return True 

    return False

def joga(jogada,jogador_da_vez , tabuleiro):
    x, y = list(map(int, jogada.split()))

    if(tabuleiro[x-1][y-1] == 0): #Se é uma jogada válida
        tabuleiro[x-1][y-1] = -1 if jogador_da_vez == 1 else 1 # se o jogador_da_vez for 1 ele coloca -1 no tabuleiro
        return True
    else:
        return False

def imprime_tabuleiro(tabuleiro):
    tab = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    print("Jogo da velha")
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 1:
                tab[i][j] = 'X'
            elif tabuleiro[i][j] == -1:
                tab[i][j] = 'O'
            else:
                tab[i][j] = ' '

    print(tab[0][0], "|", tab[0][1],"|", tab[0][2], end="\n----------\n")
    print(tab[1][0], "|", tab[1][1],"|", tab[1][2], end="\n----------\n")
    print(tab[2][0], "|", tab[2][1],"|", tab[2][2])


if __name__ == "__main__":
    jogar()