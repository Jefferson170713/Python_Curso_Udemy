# [J]efferson , Eng. De Produção
from PIL import Image

img = Image.open('foto_curriculo02.jpg')

print(img.getpixel((10, 100))) # Aqui diz referente a posição do pixel em sua escala de cor.