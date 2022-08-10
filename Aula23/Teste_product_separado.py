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

for grupo in product(p, repeat=2): # coloquei enumerate somente para enumerar a quatidade
    print(grupo)

print("PARTE 1 PRODUCT ")# ordem importa, assim o número cresce.
print('*'*70)
for i, grupo in enumerate(product(p, repeat=2)): # coloquei enumerate somente para enumerar a quatidade
    print(i+1, grupo)

print("PARTE 2 PRODUCT ")# ordem importa, assim o número cresce.
print('*'*70)