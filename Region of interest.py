import cv2
import numpy as np

image = cv2.imread('images/heisenberg.jpg')
walp = cv2.imread('images/1.jpg')

walter = image[125: 500, 550: 900] #[y1: y2, x1: x2]
#image[125: 500, 1000: 1350] = walter #[y1: y2, x1: x2]
#cv2.imshow('Walter', image)

image = cv2.resize(image, (512, 512)) #resizes to row by column
walp = cv2.resize(walp, (512, 512)) #resizes to row and column

#dst = cv2.add(image, walp)
dst = cv2.addWeighted(image, 0.9, walp, 0.1, 0) #changes transperency of both images
cv2.imshow('final', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()