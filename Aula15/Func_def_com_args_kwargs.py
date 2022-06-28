"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
def func(*args, **kwargs):
    print(args)
    print(kwargs, 'Mostra vazio')
    nome = kwargs.get("Rayssa")
    print(nome)

    pass

a = ['Jefferson', 'Rayssa']
b = ['Jonas', 'Herverton']
c = [18, 26, 25, 27]
func(a, b, c, Nome='Jefferson', Idade=30)# Aqui eu estou enviando argumentos
func(a, b, c)