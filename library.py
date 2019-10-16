import cv2
import math


class Hand:

    def __init__(self, binary, masked, raw, frame):
        self.masked = masked
        self.binary = binary
        self._raw = raw
        self.frame = frame
        self.contours = []
        self.outline = self.draw_outline()
        self.fingertips = self.extract_fingertips()

    def draw_outline(self, min_area=10000, color=(0, 255, 0), thickness=2):
        contours, _ = cv2.findContours(
            self.binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        palm_area = 0
        flag = None
        cnt = None
        for (i, c) in enumerate(contours):
            area = cv2.contourArea(c)
            if area > palm_area:
                palm_area = area
                flag = i
        if flag is not None and palm_area > min_area:
            cnt = contours[flag]
            self.contours = cnt
            cpy = self.frame.copy()
            cv2.drawContours(cpy, [cnt], 0, color, thickness)
            return cpy
        else:
            return self.frame

    def extract_fingertips(self, filter_value=50):
        cnt = self.contours
        if len(cnt) == 0:
            return cnt
        points = []
        hull = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt, hull)
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            end = tuple(cnt[e][0])
            points.append(end)
        filtered = self.filter_points(points, filter_value)

        filtered.sort(key=lambda point: point[1])
        return [pt for idx, pt in zip(range(5), filtered)]

    

   
