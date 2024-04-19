import cv2 as cv

img = cv.imread('K:\\CV\\Tutorial\\Resources\\Photos\\cat_large.jpg')
# img = cv.imread('Resources/Photos/cat.jpg')
# img = cv.imread('K:\\CV\\Tutorial\\Resources\\Photos\\cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)
