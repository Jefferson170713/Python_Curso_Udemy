# [J]efferson , Eng. De Produção

tabela = [
    #['NOMES', 'VALOR', 'QUANTIDADE'],
    ['Jefferson de Almeida', 17.7, 3],
    ['Rayssa Vasconcelos', 13.3, 6],
    ['Jonas Coelho/Greco', 24.73, 9],
    ['Juliana Juh Julaien', 15.6, 7],
    ["Herverton D'Caprio Bonitão Tapioca", 19.8, 5],
]
def mostra(a):
    print('********************************')
    print(type(a))
    for i in a:
        print(i)

def orgnize(item):
    return item[1] # Aqui eu passo qual parâmetro eu quero organizar 0, 1, 2

b = tabela
mostra(b)
# agora organizando
b.sort(key=orgnize) # do maior para o menor
mostra(b)
c = tabela
c.sort(key=orgnize, reverse=True) # Do menor para o maior
mostra(c)
print(sorted(tabela, key= lambda x: x[2], reverse=True))
print(sorted(tabela, key= lambda x: x[2], reverse=False))
