# [J]efferson , Eng. De Produção

premio = [2, 3, 5, 6, 7, 8, 9, 12, 15, 18, 19, 20, 21, 22, 24]
jogada1 = [2, 3, 4, 6, 9, 10, 12, 15, 16, 18, 19, 21, 22, 23, 24]
jogada2 = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22, 24, 25]
qtd = 0
#print(len(jogada) == len(premio))
a = [1, 2, 3]
b = [2, 3, 4]

print(len(jogada2) == len(premio))



for num, x in enumerate(jogada1):
    for y in premio:
        if x == y:
            print(x, y)
            qtd +=1


print(f'Acertos : {qtd}')