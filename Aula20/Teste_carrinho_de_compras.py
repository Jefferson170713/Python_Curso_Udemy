# [J]efferson , Eng. De Produção
def mostra(a): # fiz essa função para mostrar a lista
    for x in a:
        print(x)
    print("#" * 50)

def soma(a): # Aqui eu fiz para retornar a soma do que tinha la dentro da lista
    total = 0
    for i, j in a:
        total += j
    return total
carrinho = []
carrinho.append(('Jefferson', 17.7))
carrinho.append(('Rayssa', 13.3))
carrinho.append(('Herverton', 24.6))
carrinho.append(('Allan', 18.56))
print(carrinho)
print(type(carrinho))
for x in carrinho:
    print(x)
print('*' * 50)
recebe = [(x, y) for x, y in carrinho] # list comprehension recebendo os valores de carrinho.
mostra(recebe)
var = soma(recebe)
print(var)
# Agora olha a agilidade que o python me dar, vou fazer tudo que fiz em cima com apenas uma linha de código
# para isso vou pegar o carrinho direto.
total = sum([float(j) for x, j in carrinho])
print(total)
"""
    Repare bem em como é sutíl, porém magnifico, este recurso é muito poderoso em python.
    a função sum(), traz o total somado da lista. porém só é possível porque a variável j retornar
    porém com castig para float, toda a função dentro da list comprehension(onde o for está). 
    x refere-se ao primeiro índece da variável carrinho e j ceria o valor que tem, porem quando retorna
    do for é somente os valores de j. Com uma única linha de comando. 
"""
# só para exemplificar
print('%' * 50)
for x, y in carrinho:
    print(y)