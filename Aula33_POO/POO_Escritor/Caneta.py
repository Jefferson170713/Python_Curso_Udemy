# [J]efferson , Eng. De Produção
class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def EscrevendoCaneta(self):
        print('Escrevendo com a Caneta')