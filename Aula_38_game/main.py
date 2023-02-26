# [J]efferson de almeida
from pessoa_padrao import Pessoa
from pessoa_aatributos import PessoaHabilidades

p1 = PessoaHabilidades('Jefferson', 29, 100.00, 'Masculino', 'Quebrar as coisas')
p2 = PessoaHabilidades('Rayssa', 26, 67.00, 'Feminino', 'Números')
p3 = PessoaHabilidades('Jonas', 28, 102.85, 'Masculino', 'Estudos')
p4 = PessoaHabilidades('Herverton', 25, 71.45, 'Masculino', 'Sofrer pelo Vasco')
p5 = PessoaHabilidades('Allan', 27, 95.78, 'Masculino', 'Guardar Rancor')
#print(Pessoa.lista_pessoas)
for n, p in enumerate(Pessoa.lista_pessoas):
    print(f'{n+1} : {p}')