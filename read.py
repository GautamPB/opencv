# import cv2 as cv
#
# capture = cv.VideoCapture('./videos/sample_video.mkv')
#
# while True:
#     isTrue, frame = capture.read()
#
#     cv.imshow('Video', frame)
#
#     if cv.waitKey(20) and 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()