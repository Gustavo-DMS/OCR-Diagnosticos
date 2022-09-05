import cv2 as cv
import  os
from matplotlib import pyplot as plt
import numpy as np

directory = r"D:\Desktop\OCR teste\OCR-Diagnosticos\fotos_display"

fig, ax = plt.subplots(2, 2, figsize=(8,8))
x = 0
y = 0
for filename in os.listdir(directory):
    img = cv.imread(cv.samples.findFile(fr'D:\Desktop\OCR teste\OCR-Diagnosticos\fotos_display\{filename}'))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    blur = cv.GaussianBlur(gray,(5,5),0)
    th3 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY_INV,11,2)
    edged = cv.Canny(th3, 30, 200)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    close = cv.morphologyEx(edged, cv.MORPH_CLOSE, kernel, iterations=2)
    if y == 2:
        y = 0
        x = 1

    ax[x,y].imshow(edged,'gray')
    y += 1
plt.show()
