# [J]efferson , Eng. De Produção
from dados_map import pessoas, produtos, tipo_sangue, lista_numero
# na função map, eu passo uma função e depois um item iterador
nova_list_número = map(lambda x: x*10, lista_numero)

print(nova_list_número) # para imprimir os valores, eu tenho duas opções, ou itero a lista no for
# ou  então faço o casting de list()

print(lista_numero)
a = list(nova_list_número)
print(a)
for i in a:
    print(i)
# para mostrar a nova lista, teria que ser assim, com for
#for x, y in enumerate(nova_list_número):  ASSIM não é possível.
#    print(y[i])
#for i in list(nova_list_número): ASSIM também não é possível.
#    print(i)
#for i in nova_list_número: ASSIM TAMBÉM NÃO É POSSÍVEL
#    print(list(i))
# x = list(nova_list_número) MAIS UMA VEZ, ASSIM NÃO FUNCIONA
#for i in x:
#    print(i)
for i in lista_numero:
    print(i)
