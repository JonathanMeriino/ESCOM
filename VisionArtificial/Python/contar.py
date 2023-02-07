import cv2
import numpy as np
#Colores

borde = (0,0,255) #BGR
color_texto = (0,0,0)
img = cv2.imread(".\\Images\\img3.jpg")


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(gray,kernel,iterations=1)
dilatacion = cv2.dilate(erosion,kernel,iterations=1)
gauss = cv2.GaussianBlur(dilatacion,(5,5),0)
canny = cv2.Canny(gauss,100,200)

#contornos
cnt , _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,cnt,-1,borde,2)

#Conteo de objetos
print('Numero de objetos encontrados: ',len(cnt))
text = 'Objetos encontrados: '+ str(len(cnt))
cv2.putText(img,text,(1,50),cv2.FONT_ITALIC,0.7,color_texto,2)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('erosion',erosion)
cv2.imshow('dilatacion',dilatacion)
cv2.imshow('Canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()