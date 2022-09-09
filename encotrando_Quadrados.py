import cv2 as cv
import  os
from matplotlib import pyplot as plt
import numpy as np


directory = r".\fotos_display"


x = 0
y = 0
for filename in os.listdir(directory):
    fig, ax = plt.subplots(2, 2, figsize=(8,8))
    img = cv.imread(fr'.\fotos_display\{filename}')
    # Load img, grayscale, median blur, sharpen img

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv.filter2D(blur, -1, sharpen_kernel)

    # Threshold and morph close
    thresh = cv.threshold(sharpen, 160, 255, cv.THRESH_BINARY_INV)[1]
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=2)

    # Find contours and filter using threshold area
    cnts = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 100
    max_area = 150000
    img_number = 1
    for c in cnts:
        area = cv.contourArea(c)
        if area > min_area and area < max_area:
            x,y,w,h = cv.boundingRect(c)
            ROI = img[y:y+h, x:x+w]
            cv.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
            img_number += 1



    ax[0,0].imshow(img,'gray')
    ax[0,1].imshow(sharpen,'gray')
    ax[1,0].imshow(thresh,'gray')
    ax[1,1].imshow(close,'gray')

plt.show()
