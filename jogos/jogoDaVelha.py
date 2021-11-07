def jogo_da_velha():
    tabuleiro = [[0,0,1], [0,1,0], [1,0,0]]

    imprime_tabuleiro(tabuleiro)
    print(check_status_jogo(tabuleiro))


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
    jogo_da_velha()