# [J]efferson , Eng. De Produção
import numpy as np

class CALCULADORA:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def verificador(self):
        a = bool()
        if self.num2 == 0:
            print(f'O valor {self.num2} não pode ser zero como DIVIDENDO.')
            a = False
        else:
            print(f'{self.num2} não é igual a zero.')
            a = True
        return a

    def soma(self):
        print(f'{self.num1} + {self.num2} = ({self.num1 + self.num2})' )

    def subtracao(self):
        print(f'{self.num1} - {self.num2} = ({self.num1 - self.num2})')

    def multiplicacao(self):
        print(f'{self.num1} * {self.num2} = ({self.num1 * self.num2})')

    def divisao(self):
        div = self.verificador()
        if div == True:
            print(f'{self.num1} / {self.num2} = ({self.num1 / self.num2})')
        else:
            print('NÃO É POSSÍVEL EFETUAR A DIVISÃO.')
    def raizQuadrada(self):
        print(f'O número {self.num1} tem Raiz = {np.sqrt(self.num1)}')
        print(f'O número {self.num2} tem Raiz = {np.sqrt(self.num2)}')