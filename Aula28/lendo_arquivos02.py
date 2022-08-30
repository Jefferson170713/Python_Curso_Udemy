# [J]efferson , Eng. De Produção
# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/library/functions.html
import random

def aleatorio(int):
    int = random.randint(1, 100)
    return int
a = int()
with open('arc02.txt', 'w+') as arquivo:
    for i in range(1, 11, 1):
        a = aleatorio(a)
        arquivo.write(f'Número: {a} ' + f'Linha : {i}\n')
    arquivo.seek(0)
    print(arquivo.read())


