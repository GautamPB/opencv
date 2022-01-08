import cv2 as cv

capture = cv.VideoCapture('./videos/sample_video.mkv')

def resizeFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    frame_resized = resizeFrame(frame)
    
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()