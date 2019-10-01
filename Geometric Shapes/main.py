import cv2

img = cv2.imread('usercustom.png', 1)
# print(img)

# Line draw

# img = cv2.line(img, (0, 0), (255, 255), (0, 255, 255), 5)
# img = cv2.arrowedLine(img, (0, 255), (255, 270), (0, 255, 255), 3)

# Draw Rectangle

# img = cv2.rectangle(img,(0, 0), (255, 255), (0, 255, 255), 5);
# filling the rectangle
# img = cv2.rectangle(img,(0, 0), (255, 255), (0, 255, 255), -1);

# Draw Circle

img = cv2.circle(img, (100, 100), 100, (0, 0, 255), 5)

# Draw
font = cv2.FONT_HERSHEY_SIMPLEX
Img = cv2.putText(img, 'OpenCV', (10,100), font, 4, (0,255,255), 10, cv2.LINE_AA)

cv2.imshow('image1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()