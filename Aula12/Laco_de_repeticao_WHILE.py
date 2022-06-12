"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# WHILE -> siginifica faça então, enquanto uma determinada condição não for atendida, o laço vai se repetir!
valid = True
cont = 0
x = str(input("Digite um número: "))
if x.isdigit():
    x = int(x)
    if x > 0:
        cont = x*10
        while valid:
            print(f"{x}")
            x += 1
            if x == cont:
                valid = False
    else:
        print("O número que você digitou precisa ser MAIOR que 0", end='!')
else:
    print(f"Você não digitou um Número, Digitou isso [ {x} ]", end="!")


