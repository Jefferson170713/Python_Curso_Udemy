# [J]efferson , Eng. De Produção
from random import randint as rd
class Numero:
    def __init__(self, num=0):
        self.num = num

    def mostraNumeroAleatorio(self):
        self.num = rd(0, 10)
        return print(self.num)

    @classmethod
    def mostrarNumAleatorio(cls, num1, num2):
        num = rd(num1, num2)
        return cls(num)

    @staticmethod
    def mostrarShow():
        return rd(100, 200)


    def mostraar(self):
        return print(self)

num = Numero() # posso enviar ou não, tanto faz.

num.mostraNumeroAleatorio()

numero = Numero.mostrarNumAleatorio(10, 20)
numero.mostraar()
nume = Numero()
print(nume.mostrarShow())
