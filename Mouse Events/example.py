# drawing multiple points as a line

import cv2
import numpy as np

def drawLine(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if(len(points)>=2):
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)
        cv2.imshow('image', img)


img = cv2.imread('usercustom.png',1)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', drawLine)
cv2.waitKey(0)
cv2.destroyAllWindows()
