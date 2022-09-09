import cv2 as cv
import  os
from matplotlib import pyplot as plt


directory = r".\fotos_display"

fig, ax = plt.subplots(2, 2, figsize=(8,8))
k = 0
l = 0
for filename in os.listdir(directory):
    img = cv.imread(fr'.\fotos_display\{filename}')


    # convert the img to grayscale, blur it, and find edges
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    edged = cv.Canny(gray, 30, 200)

    #find countour
    contorno, _ = cv.findContours(edged,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # sort by area and leave only 5 largest
    nts = sorted(contorno, key=cv.contourArea, reverse=True)[:5]

    screenCnt = None

    # iterate over contours and find which satisfy some conditions
    for c in contorno:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c,0.02*peri, True) # para imgm 1
        # approx = cv.approxPolyDP(c,0.05*peri, True) # para imgm 2
        x, y, w, h = cv.boundingRect(approx)
        if h >= 15 and len(approx) == 4:
            screenCnt = approx
            break

    # # if found
    if screenCnt is not None:
        # draw rect
        x, y, w, h = cv.boundingRect(screenCnt)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        # or draw contour
        cv.drawContours(img, [screenCnt], -1, (255, 0, 0), 3)

    if k == 2:
        k = 0
        l = 1
    print(l,k)
    ax[l,k].imshow(img,'gray')
    k += 1

plt.show()




