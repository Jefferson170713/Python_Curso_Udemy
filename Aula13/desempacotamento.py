"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
lista = ['Jefferson', 'Rayssa', 'Jonas', 'Juliana', 'Allan', 'Allana', 'Herverton']
for indice, i in enumerate(lista):
    print(indice+1, i)
# agora vamos ao desempacotamento
"""v1, v2, v3 = lista
print(v1, v2, v3)
            #Se eu colocar asim haverá um erro, então será necessário colocar de ouytr forma
            com *restante_lista
"""
v1, v2, v3, *restante_lista = lista
print(v1, v2, v3)
#poderia ser assim também
*restante_lista, v1, v2, v3 = lista
print(v1, v2, v3) #Aqui já pega os últimos
# Conclusão, pega os o *Var_qualquer pega o restante da lista e transforma nume outra lista
v1 , v2, v3, *var_qualquer = lista
print(v1, v2, v3, var_qualquer)