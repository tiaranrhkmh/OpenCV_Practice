import cv2
from numpy import pi
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pic = cv2.imread('pictures\image_1.jpg')
pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)

hImg,wImg,_=pic.shape
box = pytesseract.image_to_boxes(pic)
for a in box.splitlines():
    a=a.split(' ')
    print(a)
    x,y,w,h = int(a[1]),int(a[2]),int(a[3]),int(a[4])
    cv2.rectangle(pic,(x,hImg-(y)),(x+w,wImg-h),(0,0,255),3)
    cv2.putText(pic,a[0],(x,hImg-y+100),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

cv2.imshow('Result',pic)
cv2.waitKey(0)