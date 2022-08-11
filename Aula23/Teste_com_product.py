# [J]efferson , Eng. De Produção
from itertools import product
import testes

p = testes.pessoas

teste = list()
cont = int(0)

for i, grupo in enumerate(product(p, repeat=2)):
    teste = grupo
    if teste[0] == 'Jefferson' or teste[1] == 'Jefferson':
        cont += 1
        print(cont, teste)
print(' -------------------------------- Quantidade de vezes que o nome Jefferson --------------------------')
print('*'*80)

for i, grupo in enumerate(product(p, repeat=2)):
    print(i+1, grupo)

