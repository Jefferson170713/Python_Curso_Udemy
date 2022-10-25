# [J]efferson , Eng. De Produção
from Classes import Pessaoa
from Classes import Treino
from Classes import Boxe

pessoa = Pessaoa('Jeffeson')
treinando = Treino('Treino de perna')
print(pessoa.nome)
print(treinando.treino)
pessoa_treinamento = Treino('Treino de Peito')
print(pessoa_treinamento.treino)
pessoa_treinamento.Treinando()
#pessoa_treinamento.Treinando = Boxe()
#pessoa_treinamento.tipo_de_treino = Boxe()
t = Treino('Treino de Braço')
print(t.treino)
t.Treinando()
t.tipo_de_treino = Boxe()
t.Treinando()