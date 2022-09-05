import cv2 as cv

img = cv.imread(cv.samples.findFile(r'D:\Desktop\OCR teste\OCR-Diagnosticos\fotos_display\Termometro_digital_1.png'))

# convert the image to grayscale, blur it, and find edges
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.bilateralFilter(gray, 11, 17, 17)
edged = cv.Canny(gray, 30, 200)

dst = cv.cornerHarris(edged,2,3,0.04)
# img[dst>0.01*dst.max()]=[0,0,255]
# contorno = cv.findContours(dst,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


	
blue, green, red = cv.split(img)


cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)
cv.imshow('img',img)
 
cv.waitKey(0)
cv.destroyAllWindows()
