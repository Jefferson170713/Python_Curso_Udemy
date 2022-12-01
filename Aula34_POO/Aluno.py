# [J]efferson , Eng. De Produção
from Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, num_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_class = num_class

    def falar_nome_Classe(self):
        print(f'{self.nome} {self.sobrenome} é da classe'
              f' {self.__class__.__name__}, número da classe'
              f' : {self.num_class}')
