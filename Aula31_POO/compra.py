# [J]efferson , Eng. De Produção
from random import randint as rd
class Produto:
    def __init__(self, produto, preco=50, percentual=0):
        self.produto = produto
        self.preco = preco
        self.percentual = percentual

    def Desconto(self):
        self.percentual = rd(1, 100)
        self.preco = self.preco - (self.preco * (self.percentual / 100))
        return
