# [J]efferson , Eng. De Produção
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.nomeClasse = self.__class__.__name__

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade

    def mostraClasse(self):
        print(f'A pessoa chamda: {self.__nome} Pertence a Classe: {self.nomeClasse}')

