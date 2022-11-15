# [J]efferson , Eng. De Produção
from Endereço import ENDEREÇO
class PESSOA:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.endereço = []

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade

    def insereEndereço(self, cidade, estado):
        end = ENDEREÇO(cidade, estado)
        self.endereço.append(end)

    def mostraEndereço(self):
        for end in self.endereço:
            print(end.cidade, end.estado)


