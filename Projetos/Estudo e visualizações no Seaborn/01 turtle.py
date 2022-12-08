# [J]efferson , Eng. De Produção
from turtle import *
color('red', 'blue')
begin_fill()
while True:
    forward(150)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
done()