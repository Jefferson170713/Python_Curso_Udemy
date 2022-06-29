"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
def Mostra_divisor(a):
    for i in range(1, a+1, 1):
        if (a % i) == 0:
            print(i)


valor = int(input('Digite um número: '))
Mostra_divisor(valor)


