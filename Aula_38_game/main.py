# [J]efferson de almeida
from pessoa_padrao import Pessoa
from pessoa_aatributos import PessoaHabilidades

p1 = PessoaHabilidades('Jefferson', 29, 100.00, 'Masculino', 'Quebrar as coisas')
p2 = PessoaHabilidades('Rayssa', 26, 67.00, 'Feminino', 'Números')
p3 = PessoaHabilidades('Jonas', 28, 102.85, 'Masculino', 'Estudos')
p4 = PessoaHabilidades('Herverton', 25, 71.45, 'Masculino', 'Sofrer pelo Vasco')
p5 = PessoaHabilidades('Allan', 27, 95.78, 'Masculino', 'Guardar Rancor')
# nova pessoa adicionada na lista
p6 = PessoaHabilidades('Fagner Matos', 27, 71.42, 'Masculino', 'Tocar Teclado')


#print(Pessoa.lista_pessoas)
for n, p in enumerate(Pessoa.lista_pessoas):
    print(f'{n+1} : {p}')
p6.carreiracurso('Falar Inglês')
p6.carreiracurso('Habilidade em codar em Java')
print(100*'*')
for n, p in enumerate(Pessoa.lista_pessoas):
    print(f'{n+1} : {p}')