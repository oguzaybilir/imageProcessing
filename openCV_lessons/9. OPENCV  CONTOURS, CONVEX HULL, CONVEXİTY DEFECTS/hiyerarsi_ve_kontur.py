import numpy as np 
import cv2


img = cv2.imread("C:/KISISEL/pyhtonVs/goruntu_isleme/kontur/kare2.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray,(3,3))

ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY)   # ikinci olan değerle ayar yapabiliyoruz

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = []


for i in range (len(contours)):     #conturs uzunluğu kadar fonksiyonu döndericek başlama noktası 0 olacak 

    hull.append(cv2.convexHull(contours[i],False))  # koyduğumuz false  değerin indileri döndericek ,true ise değeri döndürür
    # değerleri hul içine atıcak 


bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)   #npuit8 tipi   # görüntünün en boy oranında boş tuval oluşturuyoruz

# shapin  içindeki 0 ve 1 

for i in range (len(contours)):
    cv2.drawContours(bg,contours,i,(255,0,0),5,8,hierarchy)  
    cv2.drawContours(bg,hull,i,(0,255,0),1,8)

hierarchy= hierarchy[0]

for component in zip(contours, hierarchy):
    currentContour = component[0]
    currentHierarchy = component[1]
    x,y,w,h = cv2.boundingRect(currentContour)
    print("uzunluk",len(currentHierarchy))
   
 
   ###   HİYARARŞİ RETR_TREE  DE İNDEKS 2 EN İÇ ŞEKLE ÇİZİM YAPIYOR 
   #####   İNDEKS 3 DE EN DIŞ ŞEKLE ÇİZİM YAPIYOR  

    if currentHierarchy[2]<0 :
        print("currentHierarchy[2]", currentHierarchy[2])
        # these are the innermost child components
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
    elif currentHierarchy[3] <0:
        print("currentHierarchy[3]", currentHierarchy[3])
        # these are the outermost parent components
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),1)

cv2.imshow("image",bg)    # conturlu görüntü 
cv2.imshow("hire",img)

cv2.waitKey(0)
cv2.destroyAllWindows()








                        