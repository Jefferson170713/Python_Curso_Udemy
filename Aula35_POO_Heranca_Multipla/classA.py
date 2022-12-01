# [J]efferson , Eng. De Produção

class A:
    def __init__(self, **kwargs):
        self.arg = kwargs

    def quem_sou(self):
        print(A.mro())
    def nivel_1(self):
        print(f'Está no nivél 1.')