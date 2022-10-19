# [J]efferson , Eng. De Produção
from functools import reduce
from dados_map import lista_numero, produtos
soma = reduce(lambda acumulador, item: acumulador + item, lista_numero, 0)

print(soma)

# para deixa claro que o a função reduce faz, ela acumula valores em determinados intervalos.
# você passa o acumulador, depois aalgo que recebe o valor de algo que queira somar, após isso,
# você diz que a função lambda deve retornar pra você, depois a lista de onde quer extrair os _dados e em seguida
# de qual situação começar, se é do zero ou nao!
