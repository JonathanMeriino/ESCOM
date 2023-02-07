import cv2
import numpy as np

imagen = cv2.imread('.\\Images\\img3.jpg')
gray = cv2.cvtColor(imagen,cv2.COLOR_BGRA2GRAY)
ret, th = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
contornos,jerarquia = cv2.findContours(th,cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contornos)):
    cnt = contornos[i]
    M = cv2.moments(cnt)
    #print(M)
    cX = int(M["m10"]/M["m00"])
    cY= int(M["m01"]/M["m00"])
    print(cX)
    print(cY)

    area=cv2.contourArea(cnt)
    #print(area)
    perimetro = cv2.arcLength(cnt,True)
    #print(perimetro)
    cv2.circle(imagen,(cX,cY),5,(0,255,0),-1)
    cv2.putText(imagen,"x:"+str(cX)+",y:"+str(cY),(cX,cY),1,1,(0,0,0),1)
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Image",imagen)
    cv2.waitKey(0)


cv2.imshow("th",th)
cv2.waitKey(0)
cv2.destroyAllWindows()

