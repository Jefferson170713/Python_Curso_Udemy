# [J]efferson , Eng. D2e Produção
class CalculadoraStrings:

    def __init__(self, listA):
        self.listA = listA

    def somaDadosStrings(self):
        soma = float()
        for x in self.listA:
            soma += x
        print(soma)
        return

    def calcMedia(self):
        soma = float()
        for x in self.listA:
            soma += x
        med = (soma / len(self.listA))
        print(med)
        return
