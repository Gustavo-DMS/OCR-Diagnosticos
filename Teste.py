from pydoc import apropos
import cv2 as cv

image = cv.imread(cv.samples.findFile(r'D:\Desktop\OCR teste\OCR-Diagnosticos\fotos_display\Termometro_digital_1.png'))

# convert the image to grayscale, blur it, and find edges
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
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
    approx = cv.approxPolyDP(c,0.02*peri, True) # you could tune value of 0.02
    x, y, w, h = cv.boundingRect(approx)
    if h >= 15 and len(approx) == 4:
        screenCnt = approx
        break

# # if found
if screenCnt is not None:
    # draw rect
    x, y, w, h = cv.boundingRect(screenCnt)
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    # or draw contour
    cv.drawContours(image, [screenCnt], -1, (255, 0, 0), 3)


cv.imshow("image", image)
cv.imshow("contorno", edged)
cv.waitKey(0)



