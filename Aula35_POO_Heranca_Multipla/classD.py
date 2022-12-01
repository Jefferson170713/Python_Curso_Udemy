# [J]efferson , Eng. De Produção
from classC import C
from classB import B

class D(C, B):

    def quem_sou(self):
        print(D.__mro__)