import cv2

cam = cv2.VideoCapture(0)

while True:
	ret, frame = cam.read()
	cv2.imshow("Camera", frame)
	if(cv2.waitKey(1) == 13):
		break
cv2.destroyAllWindows()
cam.release()