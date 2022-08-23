# [J]efferson , Eng. De Produção
from dados_map import lista_numero

nova_lista = [lambda x : x > 4 for x in lista_numero] # se eu fizer só assim, retorna um iterador, por isso tentaremos
# com FILTER
new_lista = filter(lambda x : x < 4, lista_numero) # aqui eu passo uma função e um dado que eu quero movimentar.
# parecida com a função map

#print(nova_lista)
#a = list(nova_lista)

b = list(new_lista)
for i in b:
    print(i)
#for i in nova_lista:
#   print(i)