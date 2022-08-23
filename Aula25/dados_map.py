# [J]efferson , Eng. De Produção
pessoas = [
    {'Nome': 'Jefferson', 'Idade': '28'},
    {'Nome': 'Rayssa', 'Idade': '25'},
    {'Nome': 'Jonas', 'Idade': '27'},
    {'Nome': 'Juliana', 'Idade': '25'},
    {'Nome': 'Herverton', 'Idade': '24'},
    {'Nome': 'Allan', 'Idade': '27'},
    {'Nome': 'Alana', 'Idade': '23'},

]
tipo_sangue = [
    {'Nome': 'Jefferson', 'Idade': '28', 'sangue': 'A'},
    {'Nome': 'Rayssa', 'Idade': '25', 'sangue': 'B'},
    {'Nome': 'Jonas', 'Idade': '27', 'sangue': 'B'},
    {'Nome': 'Juliana', 'Idade': '25', 'sangue': 'O'},
    {'Nome': 'Herverton', 'Idade': '24', 'sangue': 'A'},
    {'Nome': 'Allan', 'Idade': '27', 'sangue': 'O'},
    {'Nome': 'Alana', 'Idade': '23', 'sangue': 'AB'},
]
produtos = [
    {'nome': 'produto 1', 'preço': 14.5},
    {'nome': 'produto 2', 'preço': 10.5},
    {'nome': 'produto 3', 'preço': 12.5},
    {'nome': 'produto 4', 'preço': 11.9},
    {'nome': 'produto 5', 'preço': 17.3},
    {'nome': 'produto 6', 'preço': 22.6},
    {'nome': 'produto 7', 'preço': 35},
    {'nome': 'produto 8', 'preço': 25}
]
lista_numero = [1, 2, 3, 4, 5, 6, 7, 8]
# ********************************************************************
# [J]efferson , Eng. De Produção
from dados_map import lista_numero

nova_lista = [lambda x : x > 4 for x in lista_numero] # se eu fizer só assim, retorna um iterador, por isso tentaremos
# com FILTER
new_lista = filter(lambda x : x > 4, lista_numero) # aqui eu passo uma função e um dado que eu quero movimentar.
# parecida com a função map

#print(nova_lista)
#a = list(nova_lista)

b = list(new_lista)
for i in b:
    print(i)
#for i in nova_lista:
#   print(i)
# ********************************************************************
# [J]efferson , Eng. De Produção
from dados_map import produtos

prod = filter(lambda p : p['preço'] > 15, produtos)

for i in prod:
    print(i)
#   Com essa função filter, consigo passar uma função e uma lista
# a adiferença é que tem uma condição embutida junto.
#