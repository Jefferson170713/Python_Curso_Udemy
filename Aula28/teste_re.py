# [J]efferson , Eng. De Produção
from time import time
import re
r = time()
x = [1, 4, 7, 2]
y = [9, 10, 6, 16, 13]
print(x)
print(y)
x.sort(reverse=True)
print(x) # x.sorte precisa estar fora do print
y = sorted(x)
print(y)
w = time()

print(r, w)


