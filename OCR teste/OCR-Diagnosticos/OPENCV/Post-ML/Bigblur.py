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

num = 0
for filename in os.listdir(directory):
    fig, ax = plt.subplots(2, 2, figsize=(10,10))
    img = cv.imread(fr'.\{directory}\{filename}')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    blurg = cv.blur(gray,(150,150))
    blurc = cv.blur(img,(150,150))
    
    ax[0,0].imshow(img,'gray')
    ax[0,1].imshow(blurg,'gray')
    ax[1,0].imshow(blurc,'gray')
    ax[1,1].imshow(gray,'gray')

plt.show()