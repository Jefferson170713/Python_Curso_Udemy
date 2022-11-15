# [J]efferson , Eng. De Produção
from ClassePessoa import PessoaEscrito
from Caneta import Caneta
from Maquina import Maquina

pessoa = PessoaEscrito('Jefferson')
print(pessoa.nome)
print('*' * 100)

maquina = Maquina('IBM')# Neste momento é independente.
print(maquina.marca)
maquina.Escrevendo()
print('*' * 100)

caneta = Caneta('BIC')# Neste momento é independente.
print(caneta.marca)
caneta.Escrevendo()
print('*' * 100)

outra_pessoa = PessoaEscrito('Rayssa')# Aqui, essa outra pessoa recebeu todas as instâncias de dentro de caneta.
outra_pessoa.ferramenta = caneta
outra_pessoa.Mostrando_meu_nome()
outra_pessoa.ferramenta.Escrevendo()