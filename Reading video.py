import cv2

cam = cv2.VideoCapture(1) #default camera index depends on position of camera

#use cam.isOpened if showing a saved video file
while cam.isOpened():
    #.read() returns 2 values, true if frame is read
    # and the frame itself
    ret, frame = cam.read()

    #cam.get() gets properties of cam mentioned within parenthesis

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", gray)

    if cv2.waitKey(1) &0xFF == ord('q'): #replaces frames every 1 ms
        break
cam.release() #releases captured variables
cv2.destroyAllWindows()