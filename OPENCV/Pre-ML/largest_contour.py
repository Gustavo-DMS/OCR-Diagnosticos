import cv2 as cv
import  os
from matplotlib import pyplot as plt
import imutils
import numpy as np


directory = r".\fotos_display"
# elementos = len(os.listdir(directory))
# xAxis = int(elementos/2)

# fig, ax = plt.subplots(2, xAxis, figsize=(8,8))
# k = 0
# l = 0
for filename in os.listdir(directory):
    fig, ax = plt.subplots(2, 2, figsize=(8,8))
    img = cv.imread(fr'.\fotos_display\{filename}')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv.filter2D(gray, -1, sharpen_kernel)
    blur = cv.GaussianBlur(sharpen,(5,5),0)
    th3 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,2)
    ret, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    edged = cv.Canny(otsu,30, 300)
    cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,
	cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv.contourArea, reverse=True)
    displayCnt = None
    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.07 * peri, True)
        # if the contour has four vertices, then we have found
        # the thermostat display
        if len(approx) == 4:
            displayCnt = approx
            x, y, w, h = cv.boundingRect(displayCnt)
            cv.drawContours(img,c, -1, (255, 0, 0), 10)
            break


    ax[0,0].imshow(img,'gray')
    ax[0,1].imshow(edged,'gray')
    ax[1,0].imshow(th3,'gray')
    ax[1,1].imshow(otsu,'gray')


    # if k == xAxis:
    #     k = 0
    #     l += 1
    # print(l,k)
    # ax[l,k].imshow(img,'gray')
    # k += 1

plt.show()