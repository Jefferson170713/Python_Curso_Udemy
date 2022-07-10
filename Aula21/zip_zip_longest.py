# [J]efferson , Eng. De Produção
# zip ----> iteráveis
# zip_longest --> itertools
def fun(s):
    for i in s:
        print(i)
    return s

cidades = ['fortaleza', 'são paulo', 'rio de janeiro', 'minas gerais']
# código
estados = ['ce', 'sp', 'rj', 'mg']

cidadesEstados = zip(cidades, estados)
print(cidadesEstados) # se eu colocar pra imprimir diretamente não mostra o valor, por que é um gerador
print(cidades)
print(estados)
for cidade, estado in cidadesEstados:
    print(cidade, estado)



