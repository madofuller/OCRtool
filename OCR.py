
import os
import cv2
import pytesseract

from PIL import Image

img = cv2.imread("Toyota_Yaris Cross_Tires_References.jpg")
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold
gry = cv2.threshold(gry, 0, 255,
                    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

f_name = "{}.png".format(os.getpid())
cv2.imwrite(f_name, gry)

text = pytesseract.image_to_string(Image.open(f_name), lang='eng')

for line in text.split('\n'):
    if "215" in line:
        name = line.split('.')[1].split(',')[0]
        print(name)

os.remove(f_name)

cv2.imshow("Image", img)
cv2.imshow("Output", gry)
cv2.waitKey(0)