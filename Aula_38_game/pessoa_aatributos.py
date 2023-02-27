# [J]efferson de almeida
from pessoa_padrao import Pessoa

class PessoaHabilidades(Pessoa):
    #Lista de Pessoas com habilidades
    lista_habilidade = []
    lista_curso = []

    def __init__(self, nome: str, idade: int, peso: float, sexo: str, habilidade):
        super().__init__(nome, idade, peso, sexo)
        self.habilidade = habilidade
        self.curso = None
        PessoaHabilidades.lista_habilidade.append(self)
    def __repr__(self):
        if self.curso == None:
            return f'[Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} Kg, Sexo: {self.sexo}, Habilidade: {self.habilidade}]'
        else:
            return f'[Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} Kg, Sexo: {self.sexo}, Habilidade: {self.habilidade}, Cursos: {self.curso}]'
    def carreiracurso(self, *args):
        PessoaHabilidades.lista_curso.append(args)
        self.curso = PessoaHabilidades.lista_curso
        return self.curso
