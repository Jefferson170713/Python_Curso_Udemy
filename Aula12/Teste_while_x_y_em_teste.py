"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
x = 0
y = 0
vld1 = True
vld2 = True
cont1 = 5
cont2 = 5
while vld1:
    while vld2:
        print(f"({x},{y})")
        y += 1
        if y == cont2:
            vld2 = False
            x += 1
            y = 0
    vld2 = True
    if x == cont1:
        vld1 = False
