import cv2

img = cv2.imread('usercustom.png', 1)
# print(img)
cv2.imshow('image', img)
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('image.png', img)
