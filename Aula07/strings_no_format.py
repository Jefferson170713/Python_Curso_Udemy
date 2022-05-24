"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
nome = "Jefferson de almeida"
idade = 28
peso = 96
altura = 1.8
imc = (peso/(altura**2))
print("""
    Nome: {n}
    Idade: {i}
    Peso: {p} kg
    Altura: {a} m
    IMC: {i_:.2f}
""" .format(n = nome, i = idade,p =  peso,a = altura, i_ = imc))
