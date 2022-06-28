"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
matriz = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
def recebe(jogo, lin, col, simb):
    pass # a e b
    for i in range(3):
        for j in range(3):
            jogo[i][j] = '| |'#aqui recebe o simbolo
    return jogo
def mostra(jogo):
    for i in range(3):
        for j in range(3):
            print(jogo[i][j], end=' ')
        print()
def valid_lin_col(a):
    if (a.isnumeric()):
        a = int(a)
    else:
        print('Por favor digite somente números entre 1 e 3 !!!')
    return a
matriz = recebe(matriz)
print(matriz)
mostra(matriz)
