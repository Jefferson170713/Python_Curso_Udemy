"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# WHILE -> siginifica faça então, enquanto uma determinada condição não for atendida, o laço vai se repetir!
valid1 = True
valid2 = True
cont1 = 0
cont2 = 0
x = str(input("Digite um número: "))
y = str(input("Digite um número: "))
if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)
    if x > 0 and y > 0:
        cont1 = x*10
        cont2 = y*10
        while valid1:
            while valid2:
                print(f"Valores de (X,Y) = ({x},{y}).")
                y += 1
                if y == cont2:
                    valid2 = False
            print(valid1)
            x += 1
            if x == cont1:
                valid1 = False
    else:
        print("Os números que você digitou precisão ser MAIORES que 0", end='!')
else:
    print(f"Você não digitou Números, Digitou isso [ {x}, {y} ]", end="!")
"""
    Este programa contem um erro, preciso corrigir ainda!
"""