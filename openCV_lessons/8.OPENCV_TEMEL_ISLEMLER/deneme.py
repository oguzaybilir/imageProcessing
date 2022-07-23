import cv2
import numpy as np

img_filter = cv2.imread("C:/Users/oguza/Documents/GitHub/imageProcessing/openCV_lessons/8.OPENCV_TEMEL_ISLEMLER/klon.jpg")
#img_median = cv2.imread("C:/Users/oguza/Desktop/klon/median.png")
#img_bilateral = cv2.imread("C:/Users/oguza/Desktop/klon/bilateral.png")

blur = cv2.blur(img_filter,(11,11))

cv2.imshow("blur", blur)
cv2.imshow("original", img_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()