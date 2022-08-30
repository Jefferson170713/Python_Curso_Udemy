# [J]efferson , Eng. De Produção
import random
def aleatorio(int):
    int = random.randint(1, 100)
    return int

arquivo = open('arc.txt', 'w+')
arquivo.write('Escrevendo no meu aquivo!\n')
a = int()

for i in range(1, 11, 1):
    a = aleatorio(a)
    arquivo.write(f'Número: {a} ' + f'Linha : {i}\n')
arquivo.seek(0)
#arquivo.close()
print(arquivo.read())
arquivo.close()
# poderia ser assim também. Com isso eu não precisaria fechar o arquivo
#with open('arc.txt', 'w+') as file:
#    for i in range(1, 11, 1):
#        a = aleatorio(a)
#        arquivo.write(f'Número: {a} ' + f'Linha : {i}\n')
#    arquivo.seek(0)
#    print(arquivo.read())