"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# lista.extend(parametro) ela adiciona tudo de uma vez
# lista.clear() limpa a lista

l1 = [1, 2, 3, 4, 5, 6]
l2 = [1.2, 2.3, 3.4, 4.5, 6.7]
l3 = []
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(l1)
print("%%%%%%%%%%%%%%%%%%%%%%%%%")
print(l2)
print("#############################")
l3.extend('#####')
print(l3)
l3.insert(4, '[J]') # Se reparar bem, ele não substitui, essa função
                    # aloca todas as coisas pra frente e insereo novo valor
print(l3)
