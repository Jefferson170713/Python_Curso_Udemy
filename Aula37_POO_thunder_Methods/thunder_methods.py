# [J]efferson de almeida

class Metodos:
    def __init__(self, pontoX=0, PontoY=0):
        self.pontoX = pontoX
        self.pontoY = PontoY
#    def __str__(self):
#        return f'{self.pontoX} + {self.pontoY}'

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.pontoX}, y={self.pontoY})'



p1 = Metodos(1, 2)
p2 = Metodos(987, 456)

print(f'O ponto 1 :{p1}')
print(f'O ponto 2 :{p2}')

# Teente fazer primeiro sem o método str, na execuçã aparecerá outra coisa.