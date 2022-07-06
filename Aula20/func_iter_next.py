# [J]efferson , Eng. De Produção
def func_devolve_iteracao():
    l = list()
    for i in range(0, 11, 1):
        l.append(i)
    return l

lis = func_devolve_iteracao()
lista = iter(lis) # adciconado o valor de iteração na variável nova, agora eu posso percorrer a lista

if hasattr(lis, '__next__'):
    print(hasattr(lis, '__next__'))
else:
    print(hasattr(lis, '__next__'))

if hasattr(lista, '__next__'): # como aqui é um objeto iterador agora
    print(hasattr(lista, '__next__'))
    print(next(lista), 1)
    print(next(lista), 2)
    print(next(lista), 3)
    print(next(lista), 4)
    print(next(lista), 5)
    print(next(lista), 6)
    print(next(lista), 7)
    print(next(lista), 8)
    print(next(lista), 9)
    print(next(lista), 10)

else:
    print(hasattr(lista, '__next__'))

#n = 123456789 isso aqui não é possível
#m = iter(n)
#print(m)

n = 'jefferson iterável'
m = iter(n)
if hasattr(m, '__next__'):
    print(hasattr(m, '__next__'))
