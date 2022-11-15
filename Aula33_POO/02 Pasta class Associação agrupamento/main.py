# [J]efferson , Eng. De Produção
from Produto import Produto
from Carrinho import Carrinho

p1 = Produto('Camisa iron men', 40.00)
p2 = Produto('Camisa', 50)
p3 = Produto('Calça jeans', 65.00)
p4 = Produto('Camisa regata', 35)
p5 = Produto('Tênis', 80)

#p1.mostraProdutos()

carrinho = Carrinho()
print(carrinho)
print('*' * 80)
carrinho.inserirProdutos(p1)
carrinho.inserirProdutos(p2)
carrinho.inserirProdutos(p3)
carrinho.inserirProdutos(p4)
carrinho.inserirProdutos(p5)
carrinho.listaDeProdutos()
print('*' * 80)
print(carrinho.soma_total())
print('*' * 80)
carrinho.remove_produto()
#carrinho.remove_produto()
carrinho.listaDeProdutos()
print('*' * 80)
#carrinho.remove_carromho_selecionado(p2) # Ainda não funciona corretamente.
#carrinho.listaDeProdutos()
