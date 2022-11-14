# [J]efferson , Eng. De Produção
class ENDEREÇO:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade
    @property
    def estado(self):
        return self.__estado