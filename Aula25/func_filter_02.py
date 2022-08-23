# [J]efferson , Eng. De Produção
from dados_map import produtos

prod = filter(lambda p: p['preço'] > 20, produtos)

for i in prod:
    print(i)
#   Com essa função filter, consigo passar uma função e uma lista
# a adiferença é que tem uma condição embutida junto.
#