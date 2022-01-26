import transform
import cv2
import imutils
import sorting_contours
import numpy as np

DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 1, 0): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9
}

image = cv2.imread("ex2.jpeg")

image = imutils.resize(image,height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(7,7),1)
edged = cv2.Canny(blur,15,200,255)

cv2.imshow("image",edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnts = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None

for c in cnts:

	perimeter = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c,0.02*perimeter,True)

	if len(approx) == 4:
		displayCnt = approx 
		break

print("warp ve outputa kadar geldik")


warped = transform.four_points_transform(blur,displayCnt.reshape(4,2))
output = transform.four_points_transform(image,displayCnt.reshape(4,2))

cv2.imshow("output",output)
cv2.imshow("warped",warped)
cv2.waitKey(0)
cv2.destroyAllWindows()

thresh = cv2.threshold(warped,200,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cv2.imshow("thresholded image",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, (3,3))
thresh = cv2.dilate(thresh,(5,5),7)

cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

digitCnts = []

for c in cnts:

	(x,y,w,h) = cv2.boundingRect(c)

	if w >= 20 and (h >= 30 and h <= 40):
		digitCnts.append(c)


#digitCnts = sorting_contours.sort_contours(digitCnts,method="left-to-right")[0]
digits = []

for c in digitCnts:

	(x,y,w,h) = cv2.boundingRect(c)
	roi = thresh[y:y+h, x:x+w]

	(roiH, roiW) = roi.shape
	(dW,dH) = (int(roiW*0.25),int(roiH*0.15))
	dHC = int(roiH*0.05)


	segments = [
		((0, 0), (w, dH)),	# top
		((0, 0), (dW, h // 2)),	# top-left
		((w - dW, 0), (w, h // 2)),	# top-right
		((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
		((0, h // 2), (dW, h)),	# bottom-left
		((w - dW, h // 2), (w, h)),	# bottom-right
		((0, h - dH), (w, h))	# bottom
	]

	on = [0] * len(segments)

	print("numaralandirma asamasina geldik")

	for (i,((xA,yA),(xB,yB))) in enumerate(segments):

		segROI = roi[yA:yB, xA:xB]
		total = cv2.countNonZero(segROI)
		area = (xB-xA)*(yB-yA)

		if total / float(area) > 0.5:
			on[i] = 1


		digit = DIGITS_LOOKUP[tuple(on)]
		digits.append(digit)
		cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),1)
		cv2.putText(output, str(digit),(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,255,0),2)

print(u"{}{}.{} \u00b0C".format(*digits))


cv2.imshow("input",image)
cv2.imshow("output",output)
cv2.waitKey(0)
cv2.destroyAllWindows()


