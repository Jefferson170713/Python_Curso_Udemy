# [J]efferson , Eng. De Produção
class Produto:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def Desconto(self, percentual):
        self.valor = self.valor - (self.valor * (percentual/100))

    #Getter
    @property
    def valor(self): # Aqui eu gero o getter ou obtenho o valor, repare qe o nome da variável mudou um pouco.
        return self.valore # ficou este nome para colocar no setter

    @valor.setter
    def valor(self, preco): # Aqui é o setter, com isso, repare que é o mesmo nome da variável, também temos uma função que verifica se é str
        if isinstance(preco, str):
            preco = float(preco.replace("R$", ""))# Aqui troca o R$ po nada e ao mesmo tempo que faz o casting para float.
        self.valore = preco
        return self.valore


prod = Produto('Camisa', 45)

prod.Desconto(25)
print(prod.valor) # Como podemos ver, passei o nome e valor da classe e em seguida fiz o calculo

# Agora veremos passando de outra forma, com uma str
prod2 = Produto('Calça', '60 R$')
prod2.Desconto(25)

print(prod2.valor) # Agora o código vai funcionar perfeitamente, mesmo passando str.

