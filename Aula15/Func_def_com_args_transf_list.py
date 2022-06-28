"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# repare que aqui eu não posso repara com o "*" a função recebe
# o argumento, porém vira uma tupla e por isso seus dados não podem ser alterados
# por isso precisamos passar para um outro tipo de variável para que possámos trablhar
# uma lista


def func1(*args):
    print('Função 1')
    print(args) #reparece qie não faz distição
    print(type(args)) # porém a clas é diferente
    print("Tamanho",len(args))
    c = args[0]
    d = args[1]
    lista = c + d
    print(type(lista))
    print(lista,'\n')

def func2(*args):
    print('Função 2')
    args = list(args)
    print(args)
    print(type(args))
    print("Tamanho",len(args))
    c = args[0]
    d = args[1]
    lista = c + d
    print(type(lista))
    print(lista, '\n')

a = ['Jefferson', 'Rayssa']
b = ['Jonas', 'Herverton']
print(a, type(a))
print(b, type(b))
func1(a, b)
func2(a, b)
