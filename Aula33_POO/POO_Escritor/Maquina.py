# [J]efferson , Eng. De Produção
class Maquina:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def Escrevendo(self):
        print(f'Máquina {self.__marca} está escrevendo com a Máquina ..')
