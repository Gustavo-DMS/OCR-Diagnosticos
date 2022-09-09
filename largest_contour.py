import cv2 as cv
import  os
from matplotlib import pyplot as plt
import imutils


directory = r".\fotos_display"

fig, ax = plt.subplots(2, 2, figsize=(8,8))
k = 0
l = 0
for filename in os.listdir(directory):
    img = cv.imread(fr'.\fotos_display\{filename}')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    blur = cv.GaussianBlur(gray,(5,5),0)
    th3 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY_INV,11,2)
    edged = cv.Canny(th3, 30, 200)
    cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,
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


    if k == 2:
        k = 0
        l = 1
    print(l,k)
    ax[l,k].imshow(img,'gray')
    k += 1

plt.show()