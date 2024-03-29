"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
import turtle
w = turtle.Screen()
w.title("Spiral Helix")
w.bgcolor('black')

colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'white']

t = turtle.Pen()
t.speed(10000)

for x in range(180):
    color = colors[x % len(colors)]
    t.pencolor(color)
    t.width(x / 45 + 1)
    t.forward(x)
    t.right(79)
    #t.left(90)
    print(color)

turtle.done()


