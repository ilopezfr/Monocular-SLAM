#!/usr/bin/env python3
import time
import cv2
from display import Display

W = 1920//2
H = 1080//2

disp = Display(W, H)
orb = cv2.ORB_create()
print(dir(orb))

class FeatureExtractor(object):
    # break image into a small grid, for better tracking
    GX = 16
    GY = 16

    def __init__(self):
        self.orb = cv2.ORB_create()

    def extract(img):
        for ry in range(0, H, GY):
            for rx in range(0, W, GX):
                kp, des = orb.detectAndCompute(img[ry])



def process_frame(img):
    img = cv2.resize(img, (W,H))

    kp, des = orb.detectAndCompute(img, None)
    for p in kp:
        u, v = map(lambda x: int(round(x)), p.pt)
        cv2.circle(img, (u, v), color =(0, 255, 0), radius = 3)


    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break