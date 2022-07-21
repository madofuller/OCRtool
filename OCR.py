import cv2
import pytesseract
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np


filename = 'Toyota_Yaris Cross_Tires_References.jpg'

img = cv2.imread(filename)
h, w, _ = img.shape


boxes = pytesseract.image_to_boxes(img)use
print(pytesseract.image_to_string(img))

for b in boxes.splitlines():
	b = b.split()
	cv2.rectangle(img, ((int(b[1]), h - int(b[2]))), ((int(b[3]), h - int(b[4]))), (0, 255, 0), 2)

st.pyplot(img)