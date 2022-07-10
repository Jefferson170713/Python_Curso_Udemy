# [J]efferson , Eng. De Produção
import sys
nome1 = 'jefferson de almeida guimarães'
nome2 = 'maria rayssa vasconcelos rodrigues'
print("""
        Nome normal: {}
        Nome Maiúscula: {}
        Tamanho em bytes do nome: {}
""" .format(nome1, nome1.upper(), sys.getsizeof(nome1)))

print("""
        Nome normal: {}
        Nome Maiúscula: {}
        Tamanho em bytes do nome: {}
""" .format(nome2, nome2.upper(), sys.getsizeof(nome2)))
print("""
        Nome1 Maiúsculo: {} Tamamnho: {}
        Nome2 Maiúsculo: {} Tamanho: {}
""" .format(nome1.upper(), sys.getsizeof(nome1.upper()), nome2.upper(), sys.getsizeof(nome2.upper())))
print(int(sys.getsizeof(nome1) + sys.getsizeof(nome2)))
print(sys.getsizeof('JEFFERSON DE ALMEIDA GUIMARAES'))
print(sys.getsizeof('jefferson de almeida guimaraes'))