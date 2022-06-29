"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
def Mostra_soma(a):
    somador = 0
    for i in range(1, a+1, 1):
        somador += i
    return somador


valor = int(input('Digite um número: '))
soma = Mostra_soma(valor)
print(soma)