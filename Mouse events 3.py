import  cv2
import numpy as np

def perform_mouse_operation(event, x, y, flags, params):
    global image
    font = cv2.FONT_HERSHEY_COMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        red = image[y, x, 2]
        green = image[y, x, 1]
        blue = image[y, x, 0]
        cv2.circle(image, (x, y), 3, (255, 255, 255), 1)
        bg = np.zeros((512, 512, 3), np.uint8)
        rgb = '(' + str(red) + ', ' + str(green) + ', ' + str(blue) + ')'

        bg = cv2.putText(bg, rgb, (x, y), font, 0.5, (0, 0, 0), 1)
        bg[:] = [blue, green, red]
        cv2.imshow("Channel", bg)

image = cv2.imread('images/1.jpg')
cv2.imshow("Image", image)

cv2.setMouseCallback("Image", perform_mouse_operation)

cv2.waitKey(0)
cv2.destroyAllWindows()