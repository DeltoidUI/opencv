import cv2
import numpy as np

cap = cv2.VideoCapture('video/tekken.mp4')

while True: 
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([20,0,0])
    upper_red = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        cv2.destroyAllWindows()
        cap.release()