# [J]efferson , Eng. De Produção
from Pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, produto, valor, quantidde=1):
        super().__init__(nome, sobrenome)
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidde

    def calculaValor(self):
        return self.valor * self.quantidade

    def compra(self):
        print(f'A cliente {self.nome} {self.sobrenome} comprou um(a) {self.produto}. '
              f'No valor de: {self.valor} R$, quantidade ({self.quantidade}) '
              f'Total a pagar ({self.calculaValor()})')



    def falar_nome_Classe(self):
        print(f'{self.nome} {self.sobrenome} é da classe {self.__class__.__name__}')