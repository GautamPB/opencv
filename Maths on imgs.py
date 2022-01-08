import cv2
import numpy as np

image = cv2.imread('images/9.jpg')

cv2.imshow("Image", image)

print(image.shape) #returns a tuple which has rows, columns and number of channels
print(image.size) #returns number of pixels in the image
print(image.dtype) #returns data type of image

b, g, r = cv2.split(image) #splits image into b, g, r channels

img = cv2.merge((b, g, r))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()