# [J]efferson , Eng. De Produção
d1 = {'nome': 'Jefferson',
      'produto': 'Luva de boxe',
      'quantidade': 100,
      'valor' : 17.07
      }
a = 'marca'# input("Digite algo: ")
b = 'mks' #input("Digite algo: ")
print(d1)
d1.update({a: b})
print(d1)
for i in d1:
      print(i)
print('Mostrando a diferença *******************')
for i in d1:
      print(d1[i])
print('Mostrando a diferença *******************')

print(d1.keys())
print(d1.values())
d2 = d1.copy()
print(d1.clear())
print(d2)
lista1 = list(d2.values())
print(lista1)
lista2 = list(d2.keys())
print(lista2)
print('Mostrando a diferença *******************')
for i, j in d2.items():
      print(i ,":", j)