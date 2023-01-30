# [J]efferson , Eng. De Produção

import cv2
from PIL import Image

img = cv2.imread('foto_curriculo02.jpg')

#img.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
#img.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

print(f'Altura : {img.shape[0]}')
print(f'Largura : {img.shape[1]}')
print(f'Canais : {img.shape[2]}')

cv2.imshow('Original', img)
cv2.waitKey(0)
#cv2.destroyAllWindows()

