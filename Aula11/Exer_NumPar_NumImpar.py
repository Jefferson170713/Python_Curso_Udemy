"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
try:
    n = int(input("Digite um número: "))
    #n2 = input("Digite o segundo número: ")
    if (n % 2) == 0:
        print(f'O número [ {n} ] é par!', type(n))
    else:
        print(f'O número [ {n} ]é impar!', type(n))
    ...
except:
    print(f'Você não digitou Números!')
    ... # isso aqui significa que o programador ainda vai continuar o código aqui
        # ou você também pode usar o "pass", mas coisa


