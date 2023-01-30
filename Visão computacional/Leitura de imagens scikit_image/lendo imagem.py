# [J]efferson , Eng. De Produção
#import skimage
from skimage import io # biblioteca de manipulação de imagens

img = io.imread('foto_curriculo02.jpg') # Ler o arquivo

io.imshow(img) #auxilia para mostrar o arquivo, detalhe é que tem um prórpia janela de mostrar

io.show() # mostra o arquivo