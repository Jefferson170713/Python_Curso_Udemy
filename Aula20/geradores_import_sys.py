# [J]efferson , Eng. De Produção
import sys
lis1 = (x for x in range(25)) # com o gerador, a memório só vai crescer quando eu pedir em um for por exemplo
lis2 = [x for x in range(25)] # a medida que eu vou aumentando o valor do range() vai crescendo na memória
print(lis1) # Aqui diz que é um obejto gerador.
print(type(lis1))
print(sys.getsizeof(lis1))
print(lis2)
print(type(lis2))
print(sys.getsizeof(lis2)) # essa função com a bibliotéca sys, sys.getsizeof(variável), mostra quanto o consumo de memória

for x in lis1:
    print(x, sys.getsizeof(x))
print(sys.getsizeof(lis1))