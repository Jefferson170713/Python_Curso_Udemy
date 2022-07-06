# [J]efferson , Eng. De Produção
def func_devolve_iteracao():
    l = list()
    for i in range(1, 11, 1):
        l.append(i)
    return l
lis = func_devolve_iteracao()
l = 123456
print(lis)
# função para saber se o objeto ou tipo de variável é ou não iterável hasattr(variável, '__iter__')
if hasattr(lis, '__iter__'):
    print(hasattr(lis, '__iter__')) # retonar True
else:
    print(hasattr(lis, '__iter__'))

if hasattr(l, '__iter__'):
    print(hasattr(l, '__iter__')) # retonar True
else:
    print(hasattr(l, '__iter__'))