# [J]efferson , Eng. De Produção
class Pessoa: # é convencional instanciar uma classe com letra Maiúscula
    def __init__(self, nome, idade, treino=False, comer=False):
        self.nome = nome
        self.idade = idade
        self.comer = comer
        self.treino = treino


    def treinar(self):
        if not self.treino:
            self.treino = True
            print(f'{self.nome} está treinando!!!', self.treino)
        else:
            print(f'{self.nome} já está treinando!!!', self.treino)
        return

    def parar_treino(self):
        if not self.treino:
            print(f'{self.nome} não está treinando!', self.treino)
        else:
            self.treino = False
            print(f'{self.nome} não está treinando.', self.treino)
        return