import cv2
import numpy as np

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("cannot open camera")

while True:
    ret, frame = cam.read()
    cv2.imshow("webcam",frame)

    if cv2.waitKey(0) == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
