import argparse #gerekli kütüphaneleri import ettik
import imutils
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i","--input", required=True, help="path to input image")
ap.add_argument("-o","--output", required=True, help="path to output image")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("image",gray)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blur, 60,255,cv2.THRESH_BINARY)[1]

#resimdeki kontürleri çıkaralım

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


# kontürleri döndürelim ve giriş resmimizin üstüne çizelim
for c in cnts:
    cv2.drawContours(image,[c],-1,(0,0,255), 2)

# resmin üzerine kontürlerin sayısını yazdıralım
text = "I found {} total shapes".format(len(cnts))
cv2.putText(image,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

# çıktımızı diske yazalım

cv2.imwrite(args["output"],image)

cv2.waitKey(0)
cv2.destroyAllWindows


