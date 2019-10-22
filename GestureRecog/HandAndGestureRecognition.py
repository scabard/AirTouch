import cv2
import math
from GestureRecog.library import Hand

def detect_face(frame, block=False, colour=(0, 0, 0)):
    fill = [1, -1][block]
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    area = 0
    X = Y = W = H = 0
    for (x, y, w, h) in faces:
        if w * h > area:
            area = w * h
            X, Y, W, H = x, y, w, h
    cv2.rectangle(frame, (X - int(0.2*W), Y - int(0.1*H)), (X + W +int(0.2*W), Y + H*2), colour, fill)

def capture_histogram(source=0):
    cap = cv2.VideoCapture(source)
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (1000, 800))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Place region of the hand inside box and press `A`",
                    (5, 50), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (500, 100), (580, 180), (105, 105, 105), 2)
        # print(frame)
        box = frame[105:175, 505:575]
        # print(box)
        cv2.imshow("Capture Histogram", frame)
        key = cv2.waitKey(10)
        if key == 97:
            object_color = box
            cv2.destroyAllWindows()
            break
        if key == 27:
            cv2.destroyAllWindows()
            cap.release()
            break

    object_color_hsv = cv2.cvtColor(object_color, cv2.COLOR_BGR2HSV)
    object_hist = cv2.calcHist([object_color_hsv], [0, 1], None,
                               [12, 15], [0, 180, 0, 256])

    cv2.normalize(object_hist, object_hist, 0, 255, cv2.NORM_MINMAX)
    cap.release()
    return object_hist

def locate_object(frame, object_hist):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    object_segment = cv2.calcBackProject(
        [hsv_frame], [0, 1], object_hist, [0, 180, 0, 256], 1)

    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    cv2.filter2D(object_segment, -1, disc, object_segment)

    _, segment_thresh = cv2.threshold(
        object_segment, 70, 255, cv2.THRESH_BINARY)

    kernel = None
    eroded = cv2.erode(segment_thresh, kernel, iterations=2)
    dilated = cv2.dilate(eroded, kernel, iterations=2)
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    masked = cv2.bitwise_and(frame, frame, mask=closing)

    return closing, masked, segment_thresh

def detect_hand(frame, hist):
    detected_hand, masked, raw = locate_object(frame, hist)
    return Hand(detected_hand, masked, raw, frame)

def count_fingers(binary):
    contours,hierarchy= cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key = lambda x: cv2.contourArea(x))

    epsilon = 0.0005*cv2.arcLength(cnt,True)
    approx= cv2.approxPolyDP(cnt,epsilon,True)

    hull = cv2.convexHull(cnt)

    areahull = cv2.contourArea(hull)
    areacnt = cv2.contourArea(cnt)

    arearatio=((areahull-areacnt)/areacnt)*100

    hull = cv2.convexHull(approx, returnPoints=False)
    defects = cv2.convexityDefects(approx, hull)

    n_fing=0

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
            n_fing += 1
            cv2.circle(binary, far, 3, [255,0,0], -1)

    n_fing+=1
    # print(n_fing)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(binary,str(n_fing),(0,50), font, 2, (255,255,255), 3, cv2.LINE_AA)

    return binary, n_fing

def find_dir(binary,n_fing,hcount,vcount,hdir,vdir,com,comprev):
    movx = 0
    movy = 0
    hrecog = 0
    vrecog = 0
    if com is not None and comprev is not None:
        if com[0] > comprev[0]:
            if hdir != 1:
                hcount = 0
                hdir = 1
            movx = 1
        else:
            if hdir != 2:
                hcount = 0
                hdir = 2
            movx=2
        if com[1] > comprev[1]:
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
    font = cv2.FONT_HERSHEY_SIMPLEX
    if hcount > 5:
        hrecog = movx
        if movx == 1:
            cv2.putText(binary,'Left',(0,100), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(n_fing,'Left')
        if movx == 2:
            cv2.putText(binary,'Right',(0,100), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(n_fing,'Right')
        hcount = 0
    if vcount > 5:
        vrecog = movy
        if movy == 1:
            cv2.putText(binary,'Down',(0,150), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(n_fing,'Down')
        if movy == 2:
            cv2.putText(binary,'Up',(0,150), font, 2, (255,255,255), 3, cv2.LINE_AA)
            print(n_fing,'Up')
        vcount = 0
    return binary, hrecog, vrecog, hcount, vcount, hdir, vdir