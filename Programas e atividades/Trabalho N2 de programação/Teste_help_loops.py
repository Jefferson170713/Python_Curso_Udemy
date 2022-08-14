# [J]efferson , Eng. De Produção
valid = bool(True)
while valid == True:
    print('Testando validador:')
    teste = int(input("Digite o valor: "))
    if teste != 0:
        valid = True
    else:
        valid = False
print("O programa saiu!!!")