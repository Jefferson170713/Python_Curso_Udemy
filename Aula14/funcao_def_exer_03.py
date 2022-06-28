"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
def soma_porcetagem(a = 0, b = 0.0):
    b = (b/100)
    soma_valor_total = a + (a * b)
    return soma_valor_total
valor1 = float(input(f'Digite o peimeiro valor: '))
valor2 = float(input(f'Digite o valor do peercentual: '))
soma = soma_porcetagem(valor1, valor2)
print(soma)