import cv2
import math
import HandAndGestureRecognition

hist = HandAndGestureRecognition.capture_histogram(source=0)
cap = cv2.VideoCapture(0)
com = (-1,-1)
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

    # if com is None:
    #     print('a')
    # else:
    com1 = com
    com = hand.get_center_of_mass()

    # print(com)
    # print(com1)
    movx = 0
    movy = 0
    if com is not None and com1 is not None:
        if com[0] > com1[0]:
            if hdir != 1:
                hcount = 0
                hdir = 1
            movx = 1
        else:
            if hdir != 2:
                hcount = 0
                hdir = 2
            movx=2
        if com[1] > com1[1]:
            if vdir != 1:
                vcount = 0
                vdir = 1
            movy = 1
        else:
            if vdir != 2:
                vcount = 0
                vdir = 2
            movy=2
    hcount = hcount + 1
    vcount = vcount + 1
    # if com is None:
    #     continue

    if com:
        cv2.circle(quick_outline, com, 10, (255, 0, 0), -1)

    cv2.imshow("Hand Outline", quick_outline)

    contours,hierarchy= cv2.findContours(hand.binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key = lambda x: cv2.contourArea(x))

    epsilon = 0.0005*cv2.arcLength(cnt,True)
    approx= cv2.approxPolyDP(cnt,epsilon,True)

    hull = cv2.convexHull(cnt)

    areahull = cv2.contourArea(hull)
    areacnt = cv2.contourArea(cnt)

    arearatio=((areahull-areacnt)/areacnt)*100

    hull = cv2.convexHull(approx, returnPoints=False)
    defects = cv2.convexityDefects(approx, hull)

    l=0

    binary = hand.binary
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(approx[s][0])
        end = tuple(approx[e][0])
        far = tuple(approx[f][0])
        pt= (100,180)


        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        s = (a+b+c)/2
        ar = math.sqrt(s*(s-a)*(s-b)*(s-c))

        d=(2*ar)/a

        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        if angle <= 90 and d>30:
            l += 1
            cv2.circle(binary, far, 3, [255,0,0], -1)

    l+=1
    # print(l)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(binary,str(l),(0,50), font, 2, (255,255,255), 3, cv2.LINE_AA)

    # if movx == 1:
    #     cv2.putText(binary,'Left',(0,100), font, 2, (255,255,255), 3, cv2.LINE_AA)
    # if movx == 2:
    #     cv2.putText(binary,'Right',(0,100), font, 2, (255,255,255), 3, cv2.LINE_AA)
    # if movy == 1:
    #     cv2.putText(binary,'Down',(0,150), font, 2, (255,255,255), 3, cv2.LINE_AA)
    # if movy == 2:
    #     cv2.putText(binary,'Up',(0,150), font, 2, (255,255,255), 3, cv2.LINE_AA)

    # print('h',hcount)
    # print('v',vcount)

    if hcount > 5:
        if movx == 1:
            cv2.putText(binary,'Left',(0,100), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(l,'Left')
        if movx == 2:
            cv2.putText(binary,'Right',(0,100), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(l,'Right')
        hcount = 0
    if vcount > 5:
        if movy == 1:
            cv2.putText(binary,'Down',(0,150), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(l,'Down')
        if movy == 2:
            cv2.putText(binary,'Up',(0,150), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(l,'Up')
        vcount = 0

    # cv2.imshow("Hand Detection", hand.masked)

    # cv2.imshow("New", hand.binary)

    cv2.imshow("New", binary)

    k = cv2.waitKey(5)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()