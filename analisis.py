# Simple Thresholding 

import cv2
import numpy as np

# Importe de imagen y conversion a gris
img = cv2.imread('img-ds/1.jpg', 0)

d = img.shape # Obtener ancho y alto de imagen

w = int(d[0]/2) # Nueva altura
h = int(d[0]/2) # Nueva anchura
image = cv2.resize(img, (h, w)) # Redimension de imagen

# Creacion de umbralizacion de imagen
_,white_bit = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY)
_,black_bit = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY_INV)

# Guardado de imagenes
cv2.imwrite('img-th/1-wth.jpg', white_bit)
cv2.imwrite('img-th/1-bth.jpg', black_bit)

# Visualizacion de imagenes
cv2.imshow('ORG-IMG', img)
cv2.imshow('MOD-IMG', image)
cv2.imshow('IMG BIN - BININV', np.hstack([white_bit, black_bit]))

cv2.waitKey(0)
cv2.destroyAllWindows()