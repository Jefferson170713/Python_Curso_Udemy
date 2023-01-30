# [J]efferson , Eng. De Produção

from skimage import color, io
# Aqui ler os arquivos
img = io.imread('foto_curriculo02.jpg')

# há várias funções de modelos de cores que podemos aplicar
cinza = color.rgb2gray(img)
outra_cor = color.rgb2hed(img)

io.imshow(cinza)

#io.imshow(outra_cor) # --> basta colocar isso e mostra a imagem com outra escala de cor
io.show()