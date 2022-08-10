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
print('Parte 1, pegando somente os nomes que estão na lista em teste.py.')
print('*'*70)
for pessoa in p:  # Aqui mostra a lista dos nomes que eu coloquei em tests.
    print(pessoa)
print('*' * 70)
for i, combinacao in enumerate(combinations(p, 2)): # você passa a lista e a quantidade de pares, 2, mas poderia ser mais.
    print(i+1, combinacao)
print("PARTE 1 COMBINATION ") # A ordem não importa, por isso o número é menor
print('*'*70)
