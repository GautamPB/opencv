import cv2

cam = cv2.VideoCapture(1)

while cam.isOpened():
    ret, frame = cam.read()
    #frame = cv2.line(frame, (0, 0), (255, 255), (255, 0, 0), 10)
    #frame = cv2.arrowedLine(frame, (0, 255), (255, 255), (255, 0, 0), 10)

    frame = cv2.rectangle(frame, (20, 20), (255, 255), (0, 255, 0), 10)
    #frame = cv2.circle(frame, (255, 255), 50, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_COMPLEX
    frame = cv2.putText(frame, "Hello World", (255, 255), font, 4, (255, 255, 255), 3, cv2.LINE_AA)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()