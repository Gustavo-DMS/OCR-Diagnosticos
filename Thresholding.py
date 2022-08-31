import cv2 as cv


img = cv.imread(cv.samples.findFile(r'D:\Desktop\OCR teste\OCR-Diagnosticos\fotos_display\Termometro_digital_4.png'))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.bilateralFilter(gray, 11, 17, 17)
th3 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

cv.SimpleBlobDetector(th3)
cv.si
cv.imshow('fds',th3)
cv.imshow('lol',img)
cv.waitKey(0)
