# [J]efferson , Eng. De Produção
class TreinoBoxe:

    def __init__(self, boxe):
        self.__boxe = boxe

    @property
    def boxe(self):
        return self.__boxe

    def TreinamentoBoxe(self, nome):
        print(f'{nome} está treinando {self.__boxe}')