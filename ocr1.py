import cv2
import pytesseract

from wand.image import Image as wi

pdf= wi(filename="OCR_1.pdf", resolution=300)
img=pdf.convert('png')
img.save(filename='u.png')

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('u.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(5,5),0)

(thresh, img) = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
cv2.imwrite('u2.png',img)


#img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_AREA)

###############pdf 1
##detect boxes for each char.
himg,wimg= img.shape

p=(pytesseract.image_to_string(img))

#cong = r'--oem 1 --psm 6 '
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    #print(b[0])
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,himg-y),(w,himg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,himg-y+5),cv2.FONT_HERSHEY_COMPLEX,0.3,(50,50,255),1)

#print(p)

a1=p[(p.find('IEC')+5):(p.find('Na')-1)]
a2=p[(p.find('Loading')+9):(p.find('Total')-1)]
a3=p[(p.find('Discharge')+10):(p.find('Loose')-1)]
a4=p[(p.find('Gross')+16):(p.find('et Wt')-3)]
a5=p[(p.find('Dest')+8):(p.find('No.of Ctrs')-1)]
a6=p[(p.find('Total Pk')+14):(p.find('Discharge')-9)]
a7=p[(p.find('Loose')+14):(p.find('Gross')-2)]
a8=p[(p.find('et Wt(KGS')+12):(p.find('Dest')-12)]
a9=p[(p.find('of Ctrs')+11):(p.find('Nature')-1)]

print("IEC =",a1)
print("Port of Loading =",a2)
print("Port of Discharge =",a3)
print("Gross wt(KGS) =",a4)
print("Country of Dest =",a5)
print("Total Pkgs =",a6)
print("Loose pckts =",a7)
print("Net wt (KGS) =",a8)
print("No.of Ctrs =",a9)

##show image
cv2.imshow('Result',img)
cv2.waitKey(0)