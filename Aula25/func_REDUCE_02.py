# [J]efferson , Eng. De Produção
from functools import reduce
from dados_map import produtos

soma_valores = reduce(lambda x, y: y['preço'] + x, produtos, 0)
print(soma_valores)
# para tira a média dos valores da lista de produtos, basta fazer um len(), ou dividir por ela.

# média dos valores dos produtos
print(round(soma_valores/len(produtos), 3))
# coma função round(valor_, tamanho de casas decimais após a virgula.)
