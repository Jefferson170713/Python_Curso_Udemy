# [J]efferson , Eng. De Produção

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)