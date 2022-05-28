"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""

'''
    Operadores relacionais
    == sinal de igual entre duas vaiáveis
    > Sinal de maior
    < Sinal de menor  
    >= Sinal de maior ou igual Ou seja, duas comparações ao mesmo tempo.
    <= Sinal de menor ou igual
    != Sinal de diferente.
'''
nome = 'Jefferson De Almeida' #= str(input('Digite seu nome: '))
idade = 64 #= int(input('Digite sua idade: '))

if idade < 18:
    print(f'{nome} é menor de idade pois sua idade é {idade}', end='.\n')
elif idade >= 18 and idade <= 45:
    print(f'{nome} é maior de idade pois sua idade é {idade} e está na meia idade', end='!!!\n')
else:
    print(f'{nome} já idoso, pois sua idade é {idade}', end="!!!\n")