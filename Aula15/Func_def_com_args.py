"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# repare que aqui eu não posso repara com o "*" a função recebe
# o argumento, porém vira uma tupla e por isso seus dados não podem ser alterados
# por isso precisamos passar para um outro tipo de variável para que possámos trablhar
# uma lista


def func(*args):
    b = len(args)
    print(type(args))
    print(b)
    print(args)
    print(args[0])
    print(args[1])
    #print(args[3])
    #print(args[4])
    #print(args[5])


a = ['Jefferson', 17, 7, 'Rayssa', 13]
func(a, 'Amor')


