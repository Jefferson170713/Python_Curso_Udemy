# [J]efferson , Eng. De Produção
class PessoaEscrito:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, trabalhando):
        self.__ferramenta = trabalhando

    def Mostrando_meu_nome(self):
        print(self.__nome)