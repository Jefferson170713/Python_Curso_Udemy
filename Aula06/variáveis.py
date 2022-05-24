"""
    Começa com letras, pode ter números mas nunca começar com números, underline para espaços
"""

print("""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
""")
nome = "Jefferson de almeida"
idade = 28
peso = 96
altura = 1.8

print("""
    Nome: {}
    Idade: {}
    Peso: {} kg
    Altura: {} m
    IMC: {}
""" .format(nome,idade, peso,altura, (peso/(altura**2))))
