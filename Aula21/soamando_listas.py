# [J]efferson , Eng. De Produção
lista1 = [500, 1000, 1500, 2000, 3000, 4000]
lista2 = [500.50, 1000.55, 1250.56, 2000.58, 3000.96, 4000.98]

lista3 = zip(lista1, lista2)
for l1, l2 in lista3:
    print(f'valor 1 {l1}, valor 2 {l2} e valores somados: {l1+l2}')
print('*' * 50)
lista4 = zip(lista1, lista2)
for i, j in lista4:
    print(f'{i+j}')
