# [J]efferson , Eng. De Produção
from itertools import count
var = count(start=0, step=2.25)# A qui também aceita números de ponto flutuante
for i in var:
    print(round(i, 2))# round() arendonda o valor nas casas decimais. nesse caso duas
    if i >= 100:
        break
print('*'*50)
