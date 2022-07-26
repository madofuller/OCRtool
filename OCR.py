import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np


reader = easyocr.Reader(['en'], gpu=False)

img = cv2.imread('Toyota_Yaris Cross_Tires_References.jpg')


results = reader.readtext(img, detail=1, paragraph=False) 
for (bbox, text, prob) in results:
    
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
   

    cv2.rectangle(img, tl, br, (0, 255, 0), 2)
    cv2.putText(img, text, (tl[0], tl[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)