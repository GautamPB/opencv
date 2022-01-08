import cv2
import datetime

cam = cv2.VideoCapture(1)

font = cv2.FONT_HERSHEY_COMPLEX
#width = cam.get(3)
#height = cam.get(4)

while cam.isOpened():
    ret, frame = cam.read()
    if ret:
        date = datetime.datetime.now()  # returns current date and time
        #text = "Date: " + str() + "  Time: " + str()
        frame = cv2.putText(frame, str(date), (10, 50), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()