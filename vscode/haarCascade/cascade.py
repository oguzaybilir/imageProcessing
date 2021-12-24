import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the input image")
ap.add_argument("-x","--xml",required=True,help="path to the input image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"])

face_cascade = cv2.CascadeClassifier(args["xml"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,7) #yüz bulunacak yer, ölçeklendirme oranı, yüz arayacak kare sayısı

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),1,(0,0,255),2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
