import cv2 as cv
import  os
from matplotlib import pyplot as plt
import imutils
import numpy as np


directory = r".\fotos_crop"
# elementos = len(os.listdir(directory))
# xAxis = int(elementos/2)

# fig, ax = plt.subplots(2, xAxis, figsize=(8,8))
# k = 0
# l = 0
for filename in os.listdir(directory):
    fig, ax = plt.subplots(2, 2, figsize=(10,10))
    img = cv.imread(fr'.\{directory}\{filename}')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h,s,v = cv.split(hsv)
    blur = cv.bilateralFilter(v,9,75,75)
    th = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,2)
    th1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,2)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    close = cv.morphologyEx(th, cv.MORPH_CLOSE, kernel, iterations=2)
    close1 = cv.morphologyEx(th1, cv.MORPH_CLOSE, kernel, iterations=2)
    cnts = cv.findContours(th.copy(), cv.RETR_EXTERNAL,
	cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv.contourArea, reverse=True)
    displayCnt = None
    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.1 * peri, True)
        # if the contour has four vertices, then we have found
        # the thermostat display
        if len(approx) == 4:
            displayCnt = approx
            x, y, w, h = cv.boundingRect(displayCnt)
            cv.drawContours(img,c, -1, (255, 0, 0), 10)
            break


    ax[0,0].imshow(img,'gray')
    ax[0,1].imshow(close,'gray')
    ax[1,0].imshow(close1,'gray')
    ax[1,1].imshow(th,'gray')


    # if k == xAxis:
    #     k = 0
    #     l += 1
    # print(l,k)
    # ax[l,k].imshow(img,'gray')
    # k += 1

plt.show()