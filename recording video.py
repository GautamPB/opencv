import cv2

cam = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('Video.mp4', fourcc, 20.0, (640, 480)) #name, 4cc code - specifies video codec, fps, size

while cam.isOpened():
    ret, frame = cam.read()
    if ret:
        cv2.imshow("Camera", frame)
        output.write(frame)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
    else:
        break
cam.release()
output.release()
cv2.destroyAllWindows()