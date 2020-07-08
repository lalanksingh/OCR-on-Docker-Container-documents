import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('q.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


#img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_AREA)
#print(pytesseract.image_to_string(img))

# ##detect boxes for each char
# himg,wimg,_= img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     #print(b)
#     b = b.split(' ')
#     #print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,himg-y),(w,himg-h),(0,0,255),1)
#     cv2.putText(img,b[0],(x,himg-y+5),cv2.FONT_HERSHEY_COMPLEX,0.3,(50,50,255),1)

##detect each word
himg,wimg,_= img.shape
#cong = r'--oem 3 --psm 6 outputdata words'
boxes = pytesseract.image_to_data(img)
#print(boxes)
for x,b in enumerate(boxes.splitlines()):
    #print(b)
    if x!=0 :
        b = b.split()
        #print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0, 0, 255), 1)
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.3, (50, 50, 255), 1)


print(pytesseract.image_to_string(img))
##show image
cv2.imshow('Result',img)
cv2.waitKey(0)