import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

def drawButtons(frame, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv.rectangle(frame, button.pos, [x + w, y + h], (255, 0, 255), -1)
        cv.putText(frame, button.text, (x + 15, y + 70), cv.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    return frame

class Button:
    def __init__(self, pos, text, size = [85, 85]):
        self.pos = pos
        self.text = text
        self.size = size
    

keys = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U','I', 'O', 'P'],
['A', 'S', 'D', 'F', 'G', 'H', 'J','K', 'L', ';'],
['Z', 'X', 'C', 'V', 'B', 'N', 'M',',', '.', '/']]

buttonList = []

for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

detector = HandDetector(detectionCon=1)

while True:
    isTrue, frame = cap.read()

    frame = detector.findHands(frame)
    lmList, bboxInfo = detector.findPosition(frame)
    
    frame = drawButtons(frame, buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if (x < lmList[8][0] < x + w and y < lmList[8][1] < y + h):
                cv.rectangle(frame, button.pos, [x + w, y + h], (0, 255, 0), -1)
                cv.putText(frame, button.text, (x + 15, y + 70), cv.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)                

    cv.imshow('Camera', frame)

    cv.waitKey(1)