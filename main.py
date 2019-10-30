import cv2
import math
import pyautogui
from GestureRecog import HandAndGestureRecognition
import altEventMapping as eventMap
import configparser
config = configparser.ConfigParser()

def createEvent(genEvent):
    event = genEvent.split('+')
    for i in range(0,len(event)-1):
        pyautogui.keyDown(event[i])
    pyautogui.press(event[len(event)-1])
    for i in range(0,len(event)-1):
        pyautogui.keyUp(event[i])

createEvent('shift+r')

hist = HandAndGestureRecognition.capture_histogram(source=0)
cap = cv2.VideoCapture(0)
com = (-1,-1)
comprev = (-1,-1)
hcount = 0
hdir = 0
vcount = 0
vdir = 0
count = 0

config.read('airtouch.ini')

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

    actWin = eventMap.retActiveWin()

    if (config.has_section(actWin) and count == 0):
        if (n_fing == 4 and hrecog == 0 and vrecog == 0 and config[actWin]['gesture1'] != 'None'):
            createEvent(config[actWin]['gesture1'])
            count = 20
        if (n_fing == 3 and hrecog == 0 and vrecog == 0 and config[actWin]['gesture2'] != 'None'):
            createEvent(config[actWin]['gesture2'])
            count = 20
        if (n_fing == 2 and hrecog == 2 and config[actWin]['gesture3'] != 'None'):
            createEvent(config[actWin]['gesture3'])
            count = 5
        if (n_fing == 2 and vrecog == 1 and config[actWin]['gesture4'] != 'None'):
            createEvent(config[actWin]['gesture4'])
            count = 5
        if (n_fing == 1 and vrecog == 2 and config[actWin]['gesture5'] != 'None'):
            createEvent(config[actWin]['gesture5'])
            count = 5
        if (n_fing == 1 and vrecog == 1 and config[actWin]['gesture6'] != 'None'):
            createEvent(config[actWin]['gesture6'])
            count = 5
    # if (actWin == 'vlc'):
    #     if (n_fing == 3 and hrecog == 0 and vrecog == 0 and count == 0):
    #         pyautogui.press('space')
    #         count = 20
    #     if (n_fing == 2 and hrecog == 2 and count == 0 ):
    #         # pyautogui.keyDown('shift')
    #         pyautogui.press('right')
    #         # pyautogui.keyUp('shift')
    #         count = 5
    #     if (n_fing == 2 and hrecog == 1 and count == 0 ):
    #         # pyautogui.keyDown('shift')
    #         pyautogui.press('left')
    #         # pyautogui.keyUp('shift')
    #         count = 5
    #     if (n_fing == 1 and vrecog == 1 and count == 0 ):
    #         pyautogui.press('down')
    #         count = 5
    #     if (n_fing == 1 and vrecog == 2 and count == 0 ):
    #         pyautogui.press('up')
    #         count = 5

    if ( count != 0):
        count = count - 1

    k = cv2.waitKey(5)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
