# [J]efferson , Eng. De Produção

class A:
    var = 123 # variável da classe.
    def __init__(self):
        self.var = 321 # variável instânciada.



# devemos ter cuidado para não alterar a variável da classe, pois alterado ela, altera tudo.
a = A()
b = A()
A.var = 'Jefferson' # funciona como se fosse o padrão, caso você não instancie nenhuma variável

print(a.var)
print(b.var)
print(A.var)