import cv2
from tkinter import *

root = Tk()
root.geometry("300x300")

def photo():
    cam = cv2.VideoCapture(0)
    while(True):
        ret, img = cam.read()
        cv2.imshow("Photo", img)

        if(cv2.waitKey(0) == 13):
            break
    cv2.destroyAllWindows()
    cam.release()

def video():
    print("Hello world from video function")

frame = Frame(root)
frame.pack()

photo = Button(frame, text = "Photo", width = 8, height = 2, command = photo)
video = Button(frame, text = "Video", width = 8, height = 2, command = video)

photo.grid(row = 0, column = 0)
video.grid(row = 0, column = 1)

root.mainloop()
