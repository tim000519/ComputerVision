import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# paint
blank[200:300,300:400] = 0,255,0
cv.imshow('Blank', blank)


# rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = cv.FILLED)
cv.imshow('Blank', blank)


img = cv.imread('K:\\CV\\Tutorial\\Resources\\Photos\\cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)