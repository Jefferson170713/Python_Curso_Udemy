# [J]efferson , Eng. De Produção
from itertools import count # start=exemplo e step=exemplo você também pode colocar no count()
contador = count()
l1 = ['jefferson', 'rayssa', 'jonas', 'juliana', 'alana', 'allan', 'heverton', 'douglas', 'darlison', 'pedro henrique', 'pedro']
listNomes = [(x, y) for x, y in zip(contador, l1)]

for i, j in listNomes:
    print(i+1, j.capitalize())