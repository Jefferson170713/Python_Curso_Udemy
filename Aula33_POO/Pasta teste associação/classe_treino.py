# [J]efferson , Eng. De Produção
class Treino:
    def __init__(self, braço):
        self.__braço = braço

    @property
    def treinoPeito(self):
        return self.__braço

    def treinandoBraço(self, nome):
        print(f'{nome} está treinando {self.__braço}')