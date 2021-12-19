import argparse #GEREKLI KUTUPHANELERI IMPORT ETTIK
import imutils
import cv2

ap = argparse.ArgumentParser()  #KULLANICIDAN RESMI ALDIK
ap.add_argument("-i","--image", required = True, help = "path to the input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])  #RESME KLASIK GRAY, BLUR VE THRESHOLD TEKNİKLERİNİ UYGULADIK
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blur, 80,150,cv2.THRESH_BINARY)[1]
cv2.imshow("thresh",thresh)

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    M = cv2.moments(c)
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])

    cv2.drawContours(img, [c],-1, (0,255,0), 2)
    cv2.circle(img, (cX,cY), 7 , (255,255,255), -1)
    cv2.putText(img, "center", (cX-20, cY-20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)


    
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


