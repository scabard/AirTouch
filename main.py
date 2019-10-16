import cv2
import math
import HandAndGestureRecognition as handDetection

hist = handDetection.capture_histogram(source=0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

cap.release()
cv2.destroyAllWindows()