# [J]efferson , Eng. De Produção

from Pessoa import PESSOA


class CLIENTE(PESSOA):

    def __init__(self, nome, idade, valor, produto, quantidade=1):
        super()
        self.__valor = valor
        self.__produto = produto
        self.__quantidade = quantidade
        self.desconto = 0


    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def compra(self):
        return self.__valor


    def descontCompra(self):

        if self.__valor > 300:
            #função retorna valor com desconto
            self.__valor = self.descontoValor(self.__valor, self.__quantidade)
            self.mostrar()
            ...
        else:
            self.mostrar()
            pass

    def mostrar(self):
        print(f'{self.nome} de idade {self.idade} está comprando.')
        print(f'Produto : {self.__produto} com desconto de {self.desconto * 100} %, no valor de {self.__valor} R$.')

    def descontoValor(self, valor, quantidade):
        if self.__valor > 300:
            self.desconto = 0.3
            self.__valor = (self.__quantidade * self.__valor - (self.__valor * self.desconto))

        elif 300 > self.__valor > 200:
            self.desconto = 0.2
            self.__valor = (self.__quantidade * self.__valor - (self.__valor * self.desconto))

        elif 200 > self.__valor > 100:
            self.desconto = 0.1
            self.__valor = (self.__quantidade * self.__valor - (self.__valor * self.desconto))

        elif 100 > self.__valor > 70:
            self.desconto = 0.05
            self.__valor = (self.__quantidade * self.__valor - (self.__valor * self.desconto))

        else:
            self.desconto = 0
            self.__valor = (self.__quantidade * self.__valor - (self.__valor * self.desconto))

        return self.__valor

