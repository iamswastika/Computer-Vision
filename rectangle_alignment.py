import numpy as np
import cv2

img = cv2.imread("img.jpg")

# converting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = gray.shape

# inverse thresholding 
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

# contour detection on grayscale image
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours detected:", len(contours))

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(cnt)

        img_center, (rect_w, rect_h), angle = cv2.minAreaRect(cnt) # getting center, width, height and angle of minimal rectagular shape inside contour
        
        # for handling rectagle rotation such that width is always parallel to x-axis
        if rect_h > rect_w:
            angle = angle - 90

        # generating rotation matrix
        rot_mat = cv2.getRotationMatrix2D(img_center, angle, 1.0)
        
        # affine transformation
        result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

        # cropping rotated rectangle
        rect_1 = result[y:y+h, x:x+w]

        cv2.imshow("image", rect_1)
        cv2.waitKey(0)