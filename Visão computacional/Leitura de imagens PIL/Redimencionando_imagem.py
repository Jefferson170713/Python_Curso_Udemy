# [J]efferson , Eng. De Produção

from PIL import Image

img = Image.open('foto_curriculo02.jpg')

redimencioando_img = img.resize((400, 500)) # Aqui você passa uma tupla para modificar o tamanho

redimencioando_img.show()