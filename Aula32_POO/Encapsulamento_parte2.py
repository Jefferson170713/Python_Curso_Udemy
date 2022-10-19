# [J]efferson , Eng. De Produção

class BaseDeDados:
    def __init__(self):
        self._dados = {} # Criei um dicionário vazio

    def inserir_Cliente(self, id, nome):

        if 'Clientes' not in self._dados:
            self._dados['Clientes'] = {id: nome}
        else:
            self._dados['Clientes'].update({id : nome})

    def lista_Clientes(self):
        print('*' * 100)
        for x, y in self._dados['Clientes'].items():
            print(x ,y)

    def apaga_Clientes(self, id):
        del self._dados['Clientes'][id]

bd = BaseDeDados()
bd.inserir_Cliente(1, 'Jefferson')
bd.inserir_Cliente(2, 'Rayssa')
bd.inserir_Cliente(3, 'Jonas')
bd.lista_Clientes()
bd.inserir_Cliente(5, 'Darlison')
bd.inserir_Cliente(6, 'Pedro Bruno')
bd.inserir_Cliente(4, 'Danilo De Almeida')
bd.lista_Clientes()
bd._dados = 'Foi modificada?'
bd.lista_Clientes()