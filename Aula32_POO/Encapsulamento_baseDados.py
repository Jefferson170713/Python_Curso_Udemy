# [J]efferson , Eng. De Produção
"""
public
privat
protected
    Um detalhe é que, em outras linguágens de programação, as instâncias criadas dentro de uma classe, podem ser desses 3
    tipos, publica que todos podem ter acesso e modificar ['Exemplo 1'].
    Por conta disso, em PYTHON, por convenção, diferente das outras linguagens, usa-se '_' ou '__' para especificar
    se o objeto ou instância será público, privado ou protegido. um _ para privado e __ para procted.
    _ privado
    __ protegido

"""
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
bd.apaga_Clientes(3)
bd.lista_Clientes()
print('*'*100)
# Se eu der um db._dados = 'Jefer'
"""
['Exemplo 1'] Com isso os _dados são quebrados porque são acessados diretamente.
bd._dados = 'Jefer'
bd.lista_Clientes()
"""
# Agora coloque bd. e espere que o program sugestione, ele não aparecesá da mesma forma. A não ser que coloque _
# Porém assim cairá no mesmo erro acima citado do exemplo 1
bd.inserir_Cliente(4, 'Darlison')
bd.inserir_Cliente(4, 'Pedro Bruno')
bd.inserir_Cliente(4, 'Danilo De Almeida')
bd.lista_Clientes()
# Cuidado, no caso acima, repare que se você não mudar o id, mudará o nome que estava antes ou o último.
bd.inserir_Cliente(5, 'Darlison')
bd.inserir_Cliente(6, 'Pedro Bruno')
bd.inserir_Cliente(4, 'Danilo De Almeida')
bd.lista_Clientes()