# [J]efferson , Eng. De Produção
from classe_pessoa import Pessoa
from classe_treino import Treino
from classe_treino_boxe import TreinoBoxe

p1 = Pessoa('Jefferson')
p1.MostraNome()
p2 = Treino('Braço')
p2.treinandoBraço(p1.nome)

p3 = TreinoBoxe('Boxe')
p3.TreinamentoBoxe(p1.nome)
p1.treinandoAcademia = p3
p1.treinandoAcademia.TreinamentoBoxe('Rayssa')
