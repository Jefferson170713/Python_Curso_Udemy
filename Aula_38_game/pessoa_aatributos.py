# [J]efferson de almeida
from pessoa_padrao import Pessoa

class PessoaHabilidades(Pessoa):
    #Lista de Pessoas com habilidades
    lista_habilidade = []
    def __init__(self, nome: str, idade: int, peso: float, sexo: str, habilidade):
        super().__init__(nome, idade, peso, sexo)
        self.habilidade = habilidade
        PessoaHabilidades.lista_habilidade.append(self)
    def __repr__(self):
        return f'[Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} Kg, Sexo: {self.sexo}, Habilidade: {self.habilidade}]'
