# [J]efferson , Eng. De Produção
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        self.__treiando = None

    @property
    def nome(self):
        return self.__nome
    @property
    def treinandoAcademmia(self):
        return self.__treiando

    @treinandoAcademmia.setter
    def treinandoAcademia(self, treinando):
        self.__treiando = treinando

    # função para ação.
    def MostraNome(self):
        print(self.__nome)