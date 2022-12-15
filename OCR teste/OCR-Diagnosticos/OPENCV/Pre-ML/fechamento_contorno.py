import cv2 as cv
import  os
from matplotlib import pyplot as plt
import imutils
import numpy as np
from matplotlib.colors import hsv_to_rgb



directory = r".\fotos_display"

for filename in os.listdir(directory):
    fig, ax = plt.subplots(2, 2, figsize=(8,8))
    img = cv.imread(fr'.\fotos_display\{filename}')
    HSV_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    h,s,v = cv.split(img)
    
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h,s,v = cv.split(hsv)
    hsv_split = np.concatenate((h,s,v),axis=1)
    cv.imshow("Split HSV",hsv_split)
    cv.waitKey(0)
    cv.destroyAllWindows()


    ax[0,0].imshow(img)
    ax[0,1].imshow(h)
    ax[1,0].imshow(s)
    ax[1,1].imshow(v)

plt.show()