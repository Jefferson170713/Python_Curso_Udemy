# [J]efferson , Eng. De Produção

from PIL import Image
from PIL import ImageEnhance

img = Image.open('foto_curriculo02.jpg')

aprimoramento = ImageEnhance.Brightness(img) # MOdifica o brilho

nova_img = aprimoramento.enhance(2) # Aqui diz o grau de brilho

aprimoramento2 = ImageEnhance.Color(img) #Aqui modifica a cor

nova_img2 = aprimoramento2.enhance(2) #Aqui de grau de modificação do brilho

img.show()
nova_img.show()
nova_img2.show()