# [J]efferson , Eng. De Produção
from classe_Pessoa import Pessoa

class CLIENTE(Pessoa):

    def compra(self):
        print(f'O cliente {self.nome} de idade {self.idade} ESTÁ COMPRANDO.')