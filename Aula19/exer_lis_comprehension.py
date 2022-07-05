# [J]efferson , Eng. De Produção
lista1 = '012345678901234567890132465789012345678901234567890123465789013245678901324567890123456789'
print(len(lista1))
n = 10
string = [lista1[i: i+n] for i in range(0, len(lista1), n)]
print(string)
mostra = '.'.join(string)
print(mostra)
#for i in range(len(lista1)):
 #   print(i, lista1[i])
