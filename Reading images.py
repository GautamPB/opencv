import cv2

'''
flag values for cv2:
1: loads color image
0: loads image in gray scale
-1: loads image as it is with alpha channel
'''
img = cv2.imread('images/1.jpg', 1) #location of image, flag

cv2.imshow('Wallpaper', img) #wallpaper is the name of the window
k = cv2.waitKey(0) #time in ms (0 means it will close when user clicks close)
if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('images/wallpaper.jpg', img) #saves image in desired location
    cv2.destroyAllWindows()