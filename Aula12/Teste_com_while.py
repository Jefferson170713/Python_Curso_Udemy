"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
x = input("Digite um número: ")
if x.isdigit():
    print(x.isdigit(), end="!")

else:
    print(f"A variável [ {x} ] não é um número", end='!')

x = int(x)
if x == 0:
    print(f"A variável: [ {x} ] é 0", end='!')
else:
    print(f"A variável: [ {x} ] é diferete de 0", end='!')

