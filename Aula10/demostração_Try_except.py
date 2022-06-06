"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# num1 = input('Digite algo: ')
# num2 = input('Digite outra coisa: ')

try:
    num1 = int(input('Digite algo: '))
    num2 = int(input('Digite outra coisa: '))
    print(f'O número 1: [{num1}] e Número 2: [{num2}], a Soma é [{num1 + num2}]',end='.')
except:
    print('Erro!!! infelismente você não digitou somente números inteiros.')

"""
Função try muito interessante, porque assim, posso implementar em meus códigos sem erro aparente
Mas consegue passar para evitar erro de código
"""