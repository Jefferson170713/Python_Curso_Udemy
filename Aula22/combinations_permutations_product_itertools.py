# [J]efferson , Eng. De Produção
"""
    combinations, permutations, product - itertools
    combinação - ordem não importa
    permutação - ordem importa
    Ambos não repetem valores únicos
    produo - ordem importa e repete valores únicos
"""
from itertools import combinations, product, permutations
l1 = ['jefferson', 'rayssa', 'jonas', 'juliana']#, 'alana', 'allan', 'heverton', 'douglas', 'darlison', 'pedro henrique', 'pedro']
print("*" *70)
for i in l1:
    print(i)
print("*" *70)
for i in combinations(l1, 2):
    print(i)
print("*" *70)
for i in permutations(l1, 2):
    print(i)
print("*" *70)
for i in product(l1):
    print(i)
print("*" *70)
