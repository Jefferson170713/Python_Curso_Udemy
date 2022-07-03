# [J]efferson , Eng. De Produção
def gameStart(lista_jogo):
    for i in range(3):
        for j in range(3):
            lista_jogo[i][j] = '| |'
    return lista_jogo
def mostra_jogo(jogo):
    for i in range(3):
        for j in range(3):
            print(jogo[i][j], end='')
        print()
def verifica_jogo(jogo):
    pass
def verif_lin_col(jogo, l, c):

    pass
def recebe_simolo(simbolo1, simbolo2, jogador):
    print(simbolo1)
    print(simbolo2)
    verificador = True
    while verificador:
        while len(simbolo1) != 1:
            simbolo1 = input(f'Digiteo simbolo do jogador {jogador}: ')
            if len(simbolo1) != 1:
                print('Por favor, digite apenas um símbolo, apenas um caractere!!!')
        verificador = verifica_caractere_igual(simbolo1, simbolo2, jogador)

    return simbolo1

def verifica_caractere_igual(simbolo1, simbolo2, jogador):
    verificador = True
    if simbolo1 == simbolo2:
        print('Não pode, por favor escola outro simbolo!!!')
    else:
        verificador = False
    return verificador