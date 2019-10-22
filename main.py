import cv2
import math
from GestureRecog import HandAndGestureRecognition

hist = HandAndGestureRecognition.capture_histogram(source=0)
cap = cv2.VideoCapture(0)
com = (-1,-1)
comprev = (-1,-1)
hcount = 0
hdir = 0
vcount = 0
vdir = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    HandAndGestureRecognition.detect_face(frame, block=True)

    hand = HandAndGestureRecognition.detect_hand(frame, hist)

    custom_outline = hand.draw_outline(
        min_area=10000, color=(0, 255, 255), thickness=2)

    quick_outline = hand.outline

    for fingertip in hand.fingertips:
        cv2.circle(quick_outline, fingertip, 5, (0, 0, 255), -1)

    comprev = com
    com = hand.get_center_of_mass()

    # print(com)
    # print(comprev)
    
    if com:
        cv2.circle(quick_outline, com, 10, (255, 0, 0), -1)

    cv2.imshow("Hand Outline", quick_outline)

    binary = hand.binary

    binary, n_fing = HandAndGestureRecognition.count_fingers(binary)
    binary, hrecog, vrecog, hcount, vcount, hdir, vdir = HandAndGestureRecognition.find_dir(binary,n_fing,hcount,vcount,hdir,vdir,com,comprev)
    
    # cv2.imshow("Hand Detection", hand.masked)

    # cv2.imshow("New", hand.binary)

    cv2.imshow("New", binary)

    k = cv2.waitKey(5)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()