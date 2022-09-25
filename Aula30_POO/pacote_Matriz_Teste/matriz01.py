# [J]efferson , Eng. De Produção
from random import randint as rd
class Matrix:
    def __init__(self, A):
        self.A = A

    def MostrarMatrix(self):
        for x in self:
            print(x)
        return


    def MatrixRandomica(self, A):
        for x in self:
            for y in self:
                self.A[x][y] = rd(1, 100)

        return