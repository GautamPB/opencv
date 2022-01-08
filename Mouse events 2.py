import  cv2
import numpy as np

def perform_operation(event, x, y, flags, params):
    clicks = 0
    global image
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        image = cv2.circle(image, (x, y), 3, (255, 255, 255), -1)

        if len(points) >= 2:
            image = cv2.circle(image, (x, y), 3, (255, 255, 255), -1)
            image = cv2.line(image, points[-1], points[-2], (255, 255, 255), 3)
        cv2.imshow("Image", image)

points = []
image = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("Image", image)

cv2.setMouseCallback("Image", perform_operation)

cv2.waitKey(0)
cv2.destroyAllWindows()