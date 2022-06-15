"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
l1 = [1, 2, 3, 4, 5, 6]
l2 = [1.2, 2.3, 3.4, 4.5, 6.7]
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(l1)
print("%%%%%%%%%%%%%%%%%%%%%%%%%")
print(l2)
print("&&&&&&&&&&&&&&&&&&&&&&&&")
l3 = l2 + l1
print(l3)
print('@@@@@@@@@@@@@@@@@@@@')
l3 = l1 + l2
print(l3)
print("########################")
l1.extend('Jefferson')
print(l1)
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
l1.extend(l3)
print(l1)
lv = []
lv.extend('Jefferson de almeida')#função que extende a lista adicionando um menbro por vez
print(lv)
lv.clear() #função para limpar a lista
lv.extend(l2)# não aceita dois parametros de uma vez
print(lv)
