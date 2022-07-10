# [J]efferson , Eng. De Produção
l1 = [500, 1000, 1500, 2000, 3000, 4000]
l2 = [500.50, 1000.55, 1250.56, 2000.58, 3000.96, 4000.98]
soma = [l1 + l2 for l1, l2 in zip(l1, l2)]
print(soma)
print('*' * 50)
for i in soma:
    print(i)
print('*' * 50)

