# [J]efferson , Eng. De Produção
from PIL import Image

img = Image.open('foto_curriculo02.jpg')

rodanddo_img = img.rotate(90)

rodanddo_img.show()

"""
    Usando a biblioteca PIL para manipulação de imagens
        - usando o comando rotate para movimentar a imagem.
"""