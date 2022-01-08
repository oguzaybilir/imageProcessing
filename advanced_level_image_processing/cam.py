import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if ret is False:
        break
        
    frame = cv2.resize(frame,(640,480))
    
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(20) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()