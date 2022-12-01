# [J]efferson , Eng. De Produção
#from classB import B
from classA import A
from classB import B
class C(B, A):

    def quem_sou(self):
        print(C.__mro__)