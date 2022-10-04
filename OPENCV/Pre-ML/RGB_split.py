import cv2 as cv
import  os
from matplotlib import pyplot as plt
import imutils
import numpy as np


directory = r".\fotos_crop"



for filename in os.listdir(directory):
    fig, ax = plt.subplots(2, 2, figsize=(8,8))
    img = cv.imread(fr'.\{directory}\{filename}')
    blue, green, red = cv.split(img)
    blurb = cv.GaussianBlur(blue,(5,5),0)
    blurg = cv.GaussianBlur(green,(5,5),0)
    blurr = cv.GaussianBlur(red,(5,5),0)
    retb, otsub = cv.threshold(blurb,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    retg, otsug = cv.threshold(blurg,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    retr, otsur = cv.threshold(blurr,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    thb = cv.threshold(blue, 50, 255, cv.THRESH_BINARY)[1]
    thg = cv.threshold(green, 100, 255, cv.THRESH_BINARY)[1]
    thr = cv.threshold(red, 150, 255, cv.THRESH_BINARY)[1]
    edgedb = cv.Canny(otsub,30, 300)
    edgedg = cv.Canny(otsug,30, 300)
    edgedr = cv.Canny(otsur,30, 300)
    cntsb,_ = cv.findContours(edgedb, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cntsg,_ = cv.findContours(edgedg, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cntsr,_ = cv.findContours(edgedr, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    Drawb = cv.drawContours(img.copy(),cntsb, -1, (255, 0, 0), 3)
    Drawg = cv.drawContours(img.copy(),cntsg, -1, (0, 255, 0), 3)
    Drawr = cv.drawContours(img.copy(),cntsr, -1, (0, 0, 255), 3)


    ax[0,0].imshow(img,'gray')
    ax[0,1].imshow(edgedb,'gray')
    ax[1,0].imshow(edgedg,'gray')
    ax[1,1].imshow(edgedr,'gray')




plt.show()