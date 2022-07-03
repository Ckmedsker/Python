import pyautogui
import cv2
import numpy as np
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

sym = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '"', '*', '|',
',', '&', '<', '`', '}', '.', '=', ']', '!', '>', ';', '?', '#','$', ')', '/', ' ', '©']

IGNORE = ["camslam8", "camslam", "camslams", "baneet", "saegiii", "saber8m"]

time.sleep(2)
screenshot = pyautogui.screenshot(region=(800, 0, 900, 350))
screenshot.save("names.png")

image = cv2.imread("names.png")

names = pytesseract.image_to_string(image)
names_list = list(names)

for i, j in enumerate(names_list):
    if j == "-":
        names_list.pop(i)
        names_list.insert(i - 1, "_")
    for k in sym:
        if j == k:
            names_list.pop(i)
names = ''.join(names_list).lower()
print(names)

names = names.split("\n")
for f in IGNORE:
    for g, d in enumerate(names):
        if f == d:
            names.pop(g)
names.pop()
print(names)