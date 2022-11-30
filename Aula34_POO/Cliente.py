# [J]efferson , Eng. De Produçã0
from Pessoa import Pessoa

class Cliente(Pessoa):






    def falar_nome_Classe(self):
        print(f'{self.nome} {self.sobrenome} é da classe {self.__class__.__name__}')