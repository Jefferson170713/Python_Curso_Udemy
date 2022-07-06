# [J]efferson , Eng. De Produção
d1 = {x for x in range(10)}
print(d1)
print(type(d1))
d2 = {x: y for x, y in enumerate(range(0, 100, 5))}
print(d2)
print(type(d2))
d3 = {x**3: y**2 for x, y in enumerate(range(10))}
print(d3)
print(type(d3))
"""
    Repare que somente com uma única linha de comando eu consegui fazer quase a mesma coisa que o primeiro d
"""
d4 = {}
d4 = lambda d1 : d1*2
print(d4)
# Aqui da um erro Em d4