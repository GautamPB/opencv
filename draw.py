import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# 1. print the image a certain color
# blank[20:30, 300:400] = 0, 255, 0
# cv.imshow('Blank', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 255, 255), thickness=-1)
cv.imshow('Circle', blank)

cv.waitKey(0)