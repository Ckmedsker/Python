from mojang import MojangAPI
import requests
import pyautogui
import cv2
import numpy as np
import pytesseract
import time



api_key="8dc9d22d-f613-4ff2-96fc-c4c5515a4d22"
IGNORE = ["camslam8", "camslam", "camslams", "baneet", "saegiii", "saber8m"]
sym = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '"', '*', '|',
',', '&', '<', '`', '}', '.', '=', ']', '!', '>', ';', '?', '#','$', ')', '/', ' ', '©']

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


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


names = names.split("\n")
for f in IGNORE:
    for g, d in enumerate(names):
        if f == d:
            names.pop(g)
names.pop()


for i in names:
    uuid = MojangAPI.get_uuid(i)

    requestlink = (f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}")

    try:
        hypixel = requests.get(requestlink).json()
        star = hypixel["player"]["achievements"]["bedwars_level"]
        final_kills = hypixel["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
        final_deaths = hypixel["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
        fkdr = round(int(final_kills) / int(final_deaths), 2)

        final_kills = "{:,}".format(final_kills)
        final_deaths = "{:,}".format(final_deaths)


        print(f"{i}:\nStar: {star}⭐\nFinal Kills: {final_kills}✔\nFinal Deaths: {final_deaths}❌\nFKDR: {fkdr}\n")
    except KeyError:
        print(f"{i} not found.\n")
        pass

    time.sleep(0.1)


    # v _> u
    # w ->