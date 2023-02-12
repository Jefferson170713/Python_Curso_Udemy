# [J]efferson de almeida

class Metodos:
    def __init__(self, pontoX=0, PontoY=0):
        self.pontoX = pontoX
        self.pontoY = PontoY
    def __str__(self):
        return f'{self.pontoX} + {self.pontoY}'

    def __repr__(self): # Aqui retorna o nome dda classe e os pontos.
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.pontoX}, y={self.pontoY})'

    def __add__(self, other):#  somando com o método, se não tiver isso não soma p3
        novo_x = self.pontoX + other.pontoX
        novo_y = self.pontoY + other.pontoY
        return Metodos(novo_x, novo_y)


if __name__ == '__main__':
    p1 = Metodos(1, 2)
    p2 = Metodos(987, 456)
    p3 = p1 + p2

    print(f'O ponto 1 : {p1}')
    print(f'O ponto 2 : {p2}')
    print(f'O ponto 3 : {p3}')

# Teente fazer primeiro sem o método str, na execuçã aparecerá outra coisa.