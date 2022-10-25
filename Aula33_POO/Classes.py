# [J]efferson , Eng. De Produção
class Pessaoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Treino:

    def __init__(self, treino):
        self.__treino = treino
        self.__tipo_de_treino = None

    @property
    def treino(self):
        return self.__treino
    @property
    def tipo_de_treino(self):
        return self.__tipo_de_treino


    @tipo_de_treino.setter
    def tipo_de_treino(self, tipo_de_treino):
        self.tipo_de_treino = tipo_de_treino
    def Treinando(self):
        print('Treinando na Academia')

class Boxe:
    def Treinando(self):
        print('Treinando na Academia, Treinando Boxe!!!')