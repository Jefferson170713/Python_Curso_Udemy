"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
def saud(sauadacao = 'Olá', name='Usuário'):
    return f'{sauadacao} {name}'
a = input("Digite seu nome: ")
b = input("Digite uma saudação: ")
var = saud(name= a, sauadacao=b)
print(var)

