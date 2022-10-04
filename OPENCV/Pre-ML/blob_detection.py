# Standard imports
import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt


directory = r".\fotos_crop"


fig, ax = plt.subplots(2, 2, figsize=(8,8))
x = 0
y = 0
for filename in os.listdir(directory):
    # Read img
    img = cv.imread(fr'.\{directory}\{filename}')

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    blur = cv.GaussianBlur(gray,(5,5),0)
    th3 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,2)

    params = cv.SimpleBlobDetector_Params()

    params.filterByArea = True
    params.minArea = 100

    detector = cv.SimpleBlobDetector_create(params)
    keypoints = detector.detect(gray)

    blank = np.zeros((0, 0))
    blobs = cv.drawKeypoints(img, keypoints, blank, (0, 0, 255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


    if y == 2:
        y = 0
        x = 1

    ax[x,y].imshow(blobs,'gray')
    y += 1
plt.show()