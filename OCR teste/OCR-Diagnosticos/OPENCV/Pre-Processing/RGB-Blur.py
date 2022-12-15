import cv2 as cv
import  os
from matplotlib import pyplot as plt
import imutils
import numpy as np


directory = r"Pre-Processing\Fotos"
save = r"Pre-Processing\Fotos-post"
for filename in os.listdir(directory):
    # fig, ax = plt.subplots(2, 2, figsize=(10,10))
    img = cv.imread(fr'{directory}\{filename}')
    blurc = cv.blur(img,(5,5))
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv.filter2D(blurc, -1, sharpen_kernel)
    # gray2 = cv.bilateralFilter(img, 11, 17, 17)
    # ret, otsu = cv.threshold(gray2,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    scale_percent = 200 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
  
    # resize image
    resized = cv.resize(sharpen, dim, interpolation = cv.INTER_AREA)


    # ax[0,0].imshow(gray1,'gray')
    # ax[0,1].imshow(gray2,'gray')
    # ax[1,0].imshow(otsu,'gray')
    cv.imwrite(os.path.join(save, filename), resized)

# plt.show()
