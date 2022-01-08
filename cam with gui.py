import cv2
from tkinter import *

root = Tk()
root.geometry("300x300")

def photo():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == 97:
            name = input("enter your name: ")
            cv2.imwrite(name + ".jpg", frame)
        elif cv2.waitKey(1) == 13:
            cam.release()
            break
    cv2.destroyAllWindows()

def video():
    print("Hello world from video function")

frame = Frame(root)
frame.pack()

photo = Button(frame, text = "Photo", width = 8, height = 2, command = photo)
video = Button(frame, text = "Video", width = 8, height = 2, command = video)

photo.grid(row = 0, column = 0)
video.grid(row = 0, column = 1)

root.mainloop()
