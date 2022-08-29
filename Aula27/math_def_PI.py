# [J]efferson , Eng. De Produção
# https://docs.python.org/3/tutorial/modules.html documentação python

import math
def dobra_lista(list):
    return list * 2
def dobra_valor(a, b):
    a = [x * 3 for x in a]
    b = a
    b = [x * 2 for x in a if x%2==0]
    return a, b
def dobra_valor_com_lambda(a):
    a = [lambda x: x*2 for x in a]
    b = list(a)
    return b
def dobra_Pi(list):
    numero_PI = math.pi
    a = [round(x*3*numero_PI, 4) for x in list]

    return a


PI = math.pi
lista = [1, 2, 3, 4, 5]
print(dobra_lista(lista))
print(dobra_valor(lista, lista))
#print(list(dobra_valor_com_lambda(lista)))
#print(dobra_valor_com_lambda(lista))  # Se eu fizer somente assim, retorna um iterador.
#b = list(dobra_valor_com_lambda(lista))
#for x, i in enumerate(b):
#    print(b[x], i)
print(dobra_Pi(lista))

