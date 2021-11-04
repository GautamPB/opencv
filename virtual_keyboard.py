import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

class Button:
    def __init__(self, pos, text, size = [100, 100]):
        self.pos = pos
        self.text = text
        self.size = size
        
    def draw(self, frame):
        x, y = self.pos
        w, h = self.size
        cv.rectangle(frame, self.pos, [x + w, y + h], (255, 0, 255), -1)
        cv.putText(frame, self.text, (x + 25, y + 25), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255))
        return frame

detector = HandDetector(detectionCon=1)

while True:
    isTrue, frame = cap.read()

    frame = detector.findHands(frame)
    lmList, bboxInfo = detector.findPosition(frame)

    button = Button([100, 100], 'Q')
    frame = button.draw(frame)

    cv.imshow('Camera', frame)

    cv.waitKey(1)