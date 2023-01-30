# [J]efferson , Eng. De Produção
from PIL import Image
from PIL import ImageEnhance # Módulo para trabalhar contraste e Brilho na imagem

img = Image.open('foto_curriculo02.jpg') # Abre a imagem que você quer

aprimoramento = ImageEnhance.Contrast(img) # você instância a função para trabalhar
nova_img = aprimoramento.enhance(4) # com a função instanciada, você já pode começar as modificações
# e altera o grau com um valor.

img.show()
nova_img.show()