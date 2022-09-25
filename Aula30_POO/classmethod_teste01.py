# [J]efferson , Eng. De Produção
class Pessoa:
    def __init__(self, nome, peso, altura=1.51): # Aqui caso eu não passe altura, já tem este valor padrão.
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def mostraAtributos(self):
        print(f'O nome é : {self.nome}, com peso {self.peso} e altura {self.altura}')
        return
    @classmethod
    def displayShow(cls, nome2, peso2, altura2=1.51):
        return cls(nome2, peso2, altura2)

p = Pessoa('Jefferson', 99.8)# Aqui eu posso passar a altura também.
p.mostraAtributos()
pessoa2 = Pessoa.displayShow('Rayssa', 26, 1.61)
pessoa2.mostraAtributos()

#
#
#
#
