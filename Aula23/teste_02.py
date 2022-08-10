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
teste = list()
"""
    Nesta primeira parte eu fiz um teste muito legal para saber somente as partes que me interressa em combinação
"""
for i, grupo in enumerate(combinations(p, 2)):
    teste = grupo
    print(teste)
    print(teste[0])
    print(teste[1])
    for i in teste:
        print(i)
    break
print('*'*70)
for i, grupo in enumerate(combinations(p, 2)):
    teste = grupo
    print(teste)
    if teste[0] == 'Rayssa' and teste[1] == 'Jefferson':
        print(i+1, grupo)
    #elif teste[0] == 'Rayssa' and teste[1] == 'Jefferson':
     #   print(i + 1, grupo)
"""
Uma explicação pra isso é que a ordem não importa, por isso meu código de cima não funciona.
se fosse com permutação sim
"""