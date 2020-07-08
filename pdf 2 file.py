import cv2
import pytesseract
from wand.image import Image as wi

pdf2= wi(filename="OCR_2.pdf", resolution=700)
img2=pdf2.convert('png')
img2.save(filename='v.png')

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img2 = cv2.imread('v.png')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
#(thresh, img2) = cv2.threshold(img2, 120, 255, cv2.THRESH_BINARY)
cv2.imwrite('v2.png', img2)


#img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_AREA)


# ##detect boxes for each char
# himg2,wimg2,_= img2.shape
#
# p2=(pytesseract.image_to_string(img2))
#
# #cong = r'--oem 1 --psm 6 '
# boxes2 = pytesseract.image_to_boxes(img2)
# for b2 in boxes2.splitlines():
#     #print(b)
#     b2 = b2.split(' ')
#     #print(b[0])
#     x2,y2,w2,h2 = int(b2[1]),int(b2[2]),int(b2[3]),int(b2[4])
#     cv2.rectangle(img2,(x2,himg2-y2),(w2,himg2-h2),(0,0,255),1)
#     cv2.putText(img2,b2[0],(x2,himg2-y2+5),cv2.FONT_HERSHEY_COMPLEX,0.3,(50,50,255),1)
#

##detect each word
himg,wimg,_= img2.shape
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


print(p2)
# print(c2)
# print(e2)
m2=min(len(c2),len(e2))
n2=0
n3=0
for n1 in range(0,m2):
    print('Container',n2+1,'No. =',c2[n2])
    print('Container', n2 + 1, 'Seal No. =', e2[n2])
    if p2.count(c2[n2])==1:
        print('container', n2 + 1, 'Size =', p2[p2.index(c2[n2]) + 1])
        n2 = n2 + 1
    if p2.count(e2[n3])==1:
        d2=str(p2[p2.index(e2[n3]) + 1])
        print('container', n3 + 1, 'Date =', d2[1:],'\n')
        n3 = n3 + 1

# n3=0
# for n4 in range(0,m2):
#     if p2.count(e2[n3])==1:
#         print('container ', n3 + 1, 'Date ', p2[p2.index(e2[n3]) + 1])
#         n3 = n3 + 1



##show image
cv2.imshow('Result 2',img2)
cv2.waitKey(0)