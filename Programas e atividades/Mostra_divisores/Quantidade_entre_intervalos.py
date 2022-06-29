"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""

def quant_intervalo(a, b):
    quantidade = 0
    for i in range(a, b+1, 1):
        quantidade += 1
    pass
    return quantidade - 2
a = 1
b = 4
c = quant_intervalo(a, b)
print(c)