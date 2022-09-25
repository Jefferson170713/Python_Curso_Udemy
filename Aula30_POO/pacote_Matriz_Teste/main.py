# [J]efferson , Eng. De Produção
from random import randint as rd
class Matriz:
    def __init__(self, mat):
        self.mat = mat

    def mostra(self):
        return print(self.mat)
    def mostraFor(self):
        for x in self.mat:
            for y in self.mat:
                self.mat[x][y] = rd(10, 20)
                print(self.mat)
        return

mat = Matriz([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
#mat.mostra()
#mat.mostraFor()
a = [x for x in range(100) if not x%2 ]
print(a)
# Aqui temos um erro ao tentar passar uma matriz

