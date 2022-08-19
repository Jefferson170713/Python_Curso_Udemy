# [J]efferson , Eng. De Produção

from dados_map import pessoas, produtos, tipo_sangue, lista_numero

nova_list_número = map(lambda x: x*10, lista_numero)
lista_nova = [x for x in produtos]
for i in lista_nova:
    print(i['preço'])
print("*"*80)
# posso fazer assim também.
# como aumentar 5% dos valores dos meus produtos?

def aumenta(p):
    p['preço'] = round(p['preço'] + 1.05, 2) # A função serve para aredondar os valores em duas casas decimais.
    return p
def novo_p(p):
    p['novo preço'] = round(p['preço'] *1.1 , 2)
    return p
novo_preco = map(aumenta, produtos)

new = map(novo_p, produtos) #com isso eu conseguir adcionar uma nova chave.

for i in novo_preco:
    print(i)
print("*"*80)
for i in new:
    print(i)
