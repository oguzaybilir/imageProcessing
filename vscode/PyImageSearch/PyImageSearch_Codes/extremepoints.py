import argparse
import numpy as np
import imutils
import cv2

""""
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to the image file")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
"""""
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if ret is False:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)

    threshold = cv2.threshold(gray,45,255,cv2.THRESH_BINARY)[1]
    threshold = cv2.erode(threshold, None, iterations=2)
    threshold = cv2.dilate(threshold, None, iterations=2)

    cnts = cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmax()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])

    cv2.drawContours(frame, [c],-1,(0,255,0),2)
    cv2.circle(frame, extLeft, 8, (0,0,255),-1)
    cv2.circle(frame, extRight, 8, (0,255,0), -1)
    cv2.circle(frame, extTop, 8, (255,0,0),-1)
    cv2.circle(frame, extBot, 8, (255,255,0),-1)

    cv2.imshow("frame",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(5,5),0)

threshold = cv2.threshold(gray,45,255,cv2.THRESH_BINARY)[1]
threshold = cv2.erode(threshold, None, iterations=2)
threshold = cv2.dilate(threshold, None, iterations=2)

cnts = cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmax()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

cv2.drawContours(image, [c],-1,(0,255,0),2)
cv2.circle(image, extLeft, 8, (0,0,255),-1)
cv2.circle(image, extRight, 8, (0,255,0), -1)
cv2.circle(image, extTop, 8, (255,0,0),-1)
cv2.circle(image, extBot, 8, (255,255,0),-1)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
