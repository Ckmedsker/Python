import numpy as np
from pygame import mixer
import cv2
import time


count = 0
mixer.init()
music = ["C2.mp3", "Eb2.mp3", "Gb2.mp3", "A2.mp3", "C3.mp3"]
video = cv2.VideoCapture(0)
starttime = time.time()


while True:
    colors = ["yellow", "blue", "purple", "red", "green"]
    LB = [20, 110, 5, 136, 25]
    LG = [150, 50, 50, 87, 52]
    LR = [20, 50, 50, 111, 72]
    UB = [35, 130, 15, 180, 102]
    UG = [255, 255, 255, 255, 255]
    UR = [255, 255, 255, 255, 255]
    lower = np.array([LB[count], LG[count], LR[count]])
    upper = np.array([UB[count], UG[count], UR[count]])
    success, img = video.read()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 250:
                for i in range(0,5):
                    if count == i:
                        print(f"{colors[count]} = {music[count]}")
                        mixer.music.load(music[count])
                        mixer.music.play()
                        time.sleep(3.0 - ((time.time() - starttime) % 3.0))


    if count + 1 >= len(colors):
        count = 0
        continue
    else:
        count += 1
        
    cv2.waitKey(1)
