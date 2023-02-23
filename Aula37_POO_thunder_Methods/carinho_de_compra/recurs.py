"""
***************************** [J]efferson ********************************
"""
import numpy as np

class CAR:

    def __init__(self, cod, produto, valor, qtd=1):
        self.cod = cod
        self.produto = produto
        self.qtd = qtd
        self.valor = valor
        self.vf = None

    def soma(self):
        self.vf = (self.qtd * self.valor)
        return self.vf

    def mostrar_valor(self):
        print(f'Código do Produto: {self.cod}')
        print(f'Produto : {self.produto}')
        print(f'Valor do Produto: {round(self.valor, 3)} R$')
        print(f'Quantidade do Produto: {self.qtd} R$')
        print(f'Total: {round(self.vf, 2)}')






