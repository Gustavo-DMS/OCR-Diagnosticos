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
   
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h,s,v = cv.split(hsv)
    blur = cv.bilateralFilter(v,11,17,17)
    gaussian = cv.GaussianBlur(blur,(5,5),0)
    _ , bw = cv.threshold(blur, 127, 255, cv.THRESH_BINARY_INV)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv.filter2D(gaussian, -1, sharpen_kernel)
    th = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
    th1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
    ret, otsu = cv.threshold(sharpen,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    nome = str(num)
    # cv.imwrite(nome+".jpg",otsu)
    num += 1
    
    
    
    
    ax[0,0].imshow(img,'gray')
    ax[0,1].imshow(th,'gray')
    ax[1,0].imshow(th1,'gray')
    ax[1,1].imshow(otsu,'gray')

plt.show()