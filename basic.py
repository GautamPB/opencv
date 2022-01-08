import cv2 as cv

image = cv.imread('./images/building.jpg')
cv.imshow('Image', image)

# 1. Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur
blur = cv.GaussianBlur(image, (171,171), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Canny edge detection
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# 4. Dilated
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroded
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# 6. Resize (ignores aspect ratio)
# resized = cv.resize(image, (500, 500))
# cv.imshow('Resized', resized)

# 7. Crop
cropped = image[150:500, 100:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)