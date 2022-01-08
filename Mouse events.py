import cv2
import numpy as np

cam = cv2.VideoCapture(1)

events = [i for i in dir(cv2) if "EVENT" in i]
print(events)

def perform_operation(event, x, y, flags, params):
    global frame
    font = cv2.FONT_HERSHEY_COMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = str(x) + ', ' + str(y)
        frame = cv2.putText(frame, pos, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow("Camera", frame)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = frame[x, y, 0]
        green = frame[x, y, 1]
        red = frame[x, y, 2]
        channel = "(" + str(blue) + ', ' + str(green) + ', ' + str(red) + ')'
        frame = cv2.putText(frame, channel, (x, y), font, 0.5, (255, 255, 255), 2)
        cv2.imshow("Camera", frame)

frame = cv2.imread('images/1.jpg')
cv2.imshow("Camera", frame)

cv2.setMouseCallback('Camera', perform_operation) #used to call functions when mouse is clicked
cv2.waitKey(0)
cv2.destroyAllWindows()

'''while cam.isOpened():
    ret, frame = cam.read()

    if ret:
        cv2.imshow("Camera", frame)
        cv2.setMouseCallback("Camera", perform_operation)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()'''