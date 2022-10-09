# [J]efferson , Eng. De Produção
from random import randint as rd

class Produto:
    def __init__(self, nome, preco=0, valor=0):
        self.nome = nome
        self.preco = preco
        self.valor = valor
    def Desconto(self):
        desc = rd(1, 100) # percentual
        self.preco = rd(500, 1200)
        self.valor = self.preco - ((self.preco * desc) / 100)
        return

    @property # Getter
    def obterGetter(self):
        return self._preco