# [J]efferson , Eng. De Produção
d1 = {
    'Dicionário 1 Produto 1': 10,
    'Dicionário 1 Produto 2': 20,
    'Dicionário 1 Produto 3': 30
}
d2 = {
    'Dicionário 2 Produto 1': 100,
    'Dicionário 2 Produto 2': 200,
    'Dicionário 2 Produto 3': 300
}
for i in d1:
    print(i, d1[i])
total = sum([int(d1[x]) for x in d1])# Aqui recebe a soma total dos valores do dicionário
print(total)
print('#' * 50)
total = sum([int(d2[x]) for x in d2])
print(total)
c = [d2[x] for x in d2]
print(c)
#print(d1[x] for x in d1) isso aqui não é possível.
