# [J]efferson , Eng. De Produção
from Pessoa import PESSOA
#from Endereço import ENDEREÇO

p1 = PESSOA('Jefferson', 29)
print(p1.nome, p1.idade)

#end = ENDEREÇO('Fortaleza', 'CE')
#print(end.cidade, end.estado)

p1.insereEndereço('Maracanau', 'CE')
p1.mostraEndereço()