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
a = 3
b = 3
c = 2.0
print(f'A é do tipo = {type(a)} e B = {type(b)} e C é tipo {type(c)}', end=".\n")
print(f'Agora iremos para as comparções e exemplos', end=("."))# essa função é smente para treinar e usar
print(f'{a}, é igual {b} = {a == b}', end=".\n")
print(f'{a}, é igual {int(b)} = {a == b} usando typeCasting', end=".\n")
print(f'{a}, é maior ou igual {b} = {a >= b}', end='.\n')
print(f'{a}, é maior ou igual {c} = {a >= c}', end='.\n')
print(f'{a}, é menor ou igual {b} = {a <= b}', end='.\n')
print(f'{a}, é menor ouigual {c} = {a <= c}', end='.\n')
print(f'{a}, é diferente {b} = {a != b}', end='.\n')
print(f'{a}, é diferente {c} = {a != c}', end='.\n')


