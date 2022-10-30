import cv2

img = imread("img.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('d', imgGray)
