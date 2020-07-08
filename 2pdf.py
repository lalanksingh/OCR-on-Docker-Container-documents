import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('q.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


#img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_AREA)


##detect boxes for each char
himg,wimg,_= img.shape

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

a1=p[(p.find('EC')+4):(p.find('Name')-2)]
a2=p[(p.find('Loading')+8):(p.find('Total')-1)]
a3=p[(p.find('Discharg')+10):(p.find('Loose')-1)]
a4=p[(p.find('Gross')+16):(p.find('et Wt')-3)]
a5=p[(p.find('Dest')+8):(p.find('No.of Ctrs')-1)]
a6=p[(p.find('Total Pkgs')+14):(p.find('Discharg')-9)]
a7=p[(p.find('Loose')+14):(p.find('Gross')-1)]
a8=p[(p.find('et Wt(KGS)')+12):(p.find('Dest')-12)]
a9=p[(p.find('of Ctrs')+11):(p.find('Nature')-3)]

my=[]
#
# ##detect each word
# himg,wimg,_= img.shape
# cong = r'--oem 3 --psm 6 outputdata words'
# boxes = pytesseract.image_to_data(img,config=cong)
# #print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     #print(b)
#     if x!=0 :
#         b = b.split()
#         #print(b)
#         if len(b)==12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x,y), (w+x, h+y), (0, 0, 255), 1)
#             cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.3, (50, 50, 255), 1)
#         #my.insert(b[12])
#
#
#
#print(my)
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