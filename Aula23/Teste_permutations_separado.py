# [J]efferson , Eng. De Produção
"""
    combinations, permutations e product - itertools
    Combinação - ordem não importa
    Permutação - ordem importa
    Obs: Ambos não repetem valores únicos
    Produto - Ordem importa e repete valores únicos

"""

from testes import pessoas
from itertools import combinations, permutations, product
p = pessoas

for i, grupo in enumerate(permutations(p, 2)): # coloquei enumerate somente para enumerar a quatidade
    print(i+1, grupo)
print("PARTE 1 PERMUTATION ")# ordem importa, assim o número cresce.
print('*'*70)

# Apenas um teste
teste = list()
# porém, precisa de um contador
cont = 0 # int()
for i, grupo in enumerate(permutations(p, 2)):
    teste = grupo
    if teste[0] == 'Jefferson' and teste[1] == 'Rayssa':
        print(i+1, grupo)
        cont += 1
    elif teste[0] == 'Rayssa' and teste[1] == 'Jefferson':
        print(i + 1, grupo)
        cont += 1
    else:
        continue
print('A quantidade de é {}'.format(cont))