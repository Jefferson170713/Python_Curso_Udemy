# [J]efferson , Eng. De Produção
D1 = {'nome': 'Jefferson',
      'produto': 'Luva de boxe',
      'quantidade': 100,
      'valor' : 17.07
      }
print(D1)
print('Se eu digitar somente "i" em D1, aparecerá somente as chaves no for!')
for i in D1:
    print(i)
print('Se eu digitar somente D1[i], apareceráo o que tem dentro das chaves!')
for i in D1:
    print(D1[i])
print(f'Exemplo: vou passar a quantidade {D1["quantidade"]} vezes o produto {D1["valor"]}.')
print(f'Olhe {D1["quantidade"] * D1["valor"]}')
D1.update({'marca' : 'MKS'})
print(D1)
