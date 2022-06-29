"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
def func01(a):
    a = func02(a) # função chamará a função 2
    return a
def func02(a):
    a = a * 10 # função 2 multiplica por 10
    return a
valor = int(input('Digite um número: '))
valor = func01(valor)
print(valor)