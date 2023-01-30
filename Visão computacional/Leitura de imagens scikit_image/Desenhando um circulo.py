# [J]efferson , Eng. De Produção

import numpy as np
from skimage import io, draw

# leiura da matriz que será a imagem
img = np.zeros((200, 200), dtype=np.uint8)

# desenho de um circulo
x, y = draw.circle_perimeter(100, 100, 20)

img[x, y] = 1

io.imshow(img)
io.show()

