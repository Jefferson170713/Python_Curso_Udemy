# [J]efferson , Eng. De Produção
class Produto:
    def __init__(self, Produto, valor):
        self.__prod = Produto
        self.__valor = valor

    @property
    def prod(self):
        return self.__prod
    @property
    def valor(self):
        return self.__valor

    def mostraProdutos(self):
        print(f'Produto {self.prod} e valor {self.valor} R$.')

"""
    Aqui é o seguinte, para dar certo colocando os atributos atributos como privados, é necessário colocar getters(property)
    par funcionar.
"""