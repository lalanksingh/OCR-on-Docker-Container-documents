import cv2
import pytesseract
import os

from wand.image import Image as wi

pdf= wi(filename="OCR_1.pdf", resolution=300)
img=pdf.convert('png')
img.save(filename='u.png')

pdf2= wi(filename="OCR_2.pdf", resolution=300)
img2=pdf2.convert('png')
img2.save(filename='v.png')


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('u.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(5,5),0)

(thresh, img) = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)


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


#
# print(my)



#################pdf 2


img2 = cv2.imread('v.png')

img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img2 = cv2.GaussianBlur(img2,(7,7),0)

(thresh, img2) = cv2.threshold(img2, 150, 255, cv2.THRESH_BINARY)

##detect each word
himg,wimg= img2.shape
#cong = r'--oem 3 --psm 6 outputdata words'
boxes = pytesseract.image_to_data(img2)
#print(boxes)

p2=[]
e2=[]
c2=[]
for x2,b2 in enumerate(boxes.splitlines()):
    #print(b)
    if x2!=0 :
        #e2 = e2 + 1
        b2 = b2.split()
        #print(b2)
        if len(b2)==12:
            x2, y2, w2, h2 = int(b2[6]), int(b2[7]), int(b2[8]), int(b2[9])
            cv2.rectangle(img2, (x2,y2), (w2+x2, h2+y2), (0, 0, 255), 1)
            cv2.putText(img2, b2[11], (x2,y2), cv2.FONT_HERSHEY_COMPLEX, 0.3, (50, 50, 255), 1)
            #print(b2[11])
            p2.append(b2[11])

            # finding container no.
            if len(b2[11])==11:
                c2.append(b2[11])


            # finding container seal no.
            if len(b2[11])==12:
                e2.append(b2[11])

report=open('ocr-report.txt','w')

print("IEC =",a1)
report.write("IEC = "+a1+'\n')
print("Port of Loading =",a2)
report.write("Port of Loading = "+a2+'\n')
print("Port of Discharge =",a3)
report.write("Port of Discharge = "+a3+'\n')
print("Gross wt(KGS) =",a4)
report.write("Gross wt(KGS) = "+a4+'\n')
print("Country of Dest =",a5)
report.write("Country of Dest = "+a5+'\n')
print("Total Pkgs =",a6)
report.write("Total Pkgs = "+a6+'\n')
print("Loose pckts =",a7)
report.write("Loose pckts = "+a7+'\n')
print("Net wt (KGS) =",a8)
report.write("Net wt (KGS) = "+a8+'\n')
print("No.of Ctrs =",a9)
report.write("No.of Ctrs = "+a9+'\n'+'\n')

# print(p2)
# print(c2)
# print(e2)
m2=min(len(c2),len(e2))
n2=0
n3=0
for n1 in range(0,m2):
    print('Container',n2+1,'No. =',c2[n2])
    report.write('Container'+ str( n2+1)+' No. = '+str(c2[n2])+'\n')
    print('Container', n2 + 1, 'Seal No. =', e2[n2])
    report.write('Container'+ str( n2 + 1)+ ' Seal No. = '+str(e2[n2])+'\n')
    if p2.count(c2[n2])==1:
        print('container', n2 + 1, 'Size =', p2[p2.index(c2[n2]) + 1])
        report.write('container'+ str(n2 + 1)+' Size = '+str(p2[p2.index(c2[n2]) + 1])+'\n')
        n2 = n2 + 1
    if p2.count(e2[n3])==1:
        d2 = str(p2[p2.index(e2[n3]) + 1])
        print('container', n3 + 1, 'Date =', d2[1:], '\n')
        report.write('container'+ str(n3 + 1)+ ' Date = '+ str(d2[1:])+'\n'+'\n')
        n3 = n3 + 1




report.close()

##show image
#cv2.imshow('Result',img)


##show image
# cv2.imshow('Result 2',img2)
# cv2.waitKey(0)

os.startfile('ocr-report.txt')
