import cv2 as cv

img = cv.imread("./images/drake-1.jpg")
cv.imshow('Drake', img)
cv.waitKey(0)
