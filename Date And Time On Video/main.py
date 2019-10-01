import cv2
import datetime
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = "Width" + str(cap.get(3)) + ' Height' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
