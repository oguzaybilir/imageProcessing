import cv2
import argparse
import numpy
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)
ret, threhold = cv2.threshold(blur,90,255,cv2.THRESH_BINARY)[1]

cv2.imshow("img", img)


