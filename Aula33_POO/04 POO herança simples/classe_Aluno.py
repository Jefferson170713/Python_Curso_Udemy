# [J]efferson , Eng. De Produção
from classe_Pessoa import Pessoa

class ALUNO(Pessoa):

    def estudando(self):
        print(f'O Aluno: {self.nome} de idade: {self.idade} ESTÁ ESTUDANDO.')