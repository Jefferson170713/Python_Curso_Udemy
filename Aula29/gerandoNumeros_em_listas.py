# [J]efferson , Eng. De Produção
import random

def lista_aleatoria(lista_a, n):
    for i in range(n):
        a = random.randint(0, 10)
        r = i + a % (9 - i)
        tmp = lista_a[i]
        lista_a[i] = lista_a[r]
        lista_a[r] = tmp

listaB = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print('+'*75)
print(listaB)
lista_aleatoria(listaB, len(listaB))
print('+'*75)
print(listaB)
print('+'*75)
lista_aleatoria(listaB, len(listaB))
print(listaB)
print('+'*75)
lista_aleatoria(listaB, len(listaB))
print(listaB)
print('+'*75)
lista_aleatoria(listaB, len(listaB))
print(listaB)