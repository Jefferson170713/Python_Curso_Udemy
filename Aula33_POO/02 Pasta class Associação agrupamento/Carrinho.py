# [J]efferson , Eng. De Produção
class Carrinho:

    def __init__(self):
        self.__Carrinho = []

    def inserirProdutos(self, produto):
        self.__Carrinho.append(produto)

    def listaDeProdutos(self):
        i = 0
        for produto in self.__Carrinho:
            i += 1
            print(f'Produto ({i}): {produto.prod} | Valor: {produto.valor} R$')

    def soma_total(self):
        total = 0
        for produto in self.__Carrinho:
            total += produto.valor
        print('Soma total: ')
        return total
    def remove_produto(self):
        self.__Carrinho.pop()

    def remove_carromho_selecionado(self, produto): # Ainda não funciona corretamente.
        for Prod in self.__Carrinho:
            if Prod.prod == produto.prod:
                self.__Carrinho.remove()
        return
