# [J]efferson , Eng. De Produção

import random

teste = bool(True)
a = 0
soma = 0
while teste:
    a = random.randint(0, 1000000)
    print(a)
    if a == 100:
        print('Entrou no if e vai sair')
        teste = False
    else:
        soma += 1
print(soma)
print('Fim do programa!')