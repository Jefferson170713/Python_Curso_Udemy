# [J]efferson de almeida

class Pessoa:

    # lista para saber a quantidade de pessoas.
    lista_pessoas = []

    # Atributos padrão da classe
    def __init__(self, nome: str, idade: int, peso: float, sexo: str):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.sexo = sexo
        Pessoa.lista_pessoas.append(self)
    def __repr__(self):
        return f'[Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} Kg, Sexo: {self.sexo}]'


