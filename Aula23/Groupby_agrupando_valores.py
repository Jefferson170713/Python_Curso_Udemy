
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
#for ps in p:  # Aqui mostra a lista dos nomes que eu coloquei em tests.
#    print(ps)
for i, combinacao in enumerate(combinations(p, 2)): # você passa a lista e a quantidade de pares, 2, mas poderia ser mais.
    print(i+1, combinacao)
print("PARTE 1 COMBINATION ") # A ordem não importa, por isso o número é menor
print('*'*70)
for i, grupo in enumerate(permutations(p, 2)): # coloquei enumerate somente para enumerar a quatidade
    print(i+1, grupo)
print("PARTE 1 PERMUTATION ")# ordem importa, assim o número cresce.
print('*'*70)
for i, grupo in enumerate(product(p, repeat=2)): # coloquei enumerate somente para enumerar a quatidade
    print(i+1, grupo)
print("PARTE 1 PRODUCT ")# ordem importa, assim o número cresce. Agora repete jefferson e jefferson,
print('*'*70)