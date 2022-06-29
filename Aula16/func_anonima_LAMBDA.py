# [J]efferson , Eng. De Produção
def func(a,b):
    return a * b

a = func(2,3)
print(a)
b = lambda c, d: c *d # chamado de função anônima
print(b) # aqui ele passa somente o que é e o que tem na vriável

print(b(2, 3)) # faz a mesma coisa que a primeira função e ainda é mais simplificada

