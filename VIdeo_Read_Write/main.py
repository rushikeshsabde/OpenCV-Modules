import cv2

cap = cv2.VideoCapture('rtsp://admin:123456@172.16.25.90')
# cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))
print(cap)

while True:
    ret, frame = cap.read()
    out.write(frame)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # for making the image gray
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()