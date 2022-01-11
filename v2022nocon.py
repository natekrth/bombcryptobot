import pyautogui
import cv2
import time

def click(name):
    test = pyautogui.locateOnScreen(name, confidence=0.9)
    test2 = pyautogui.center(test)
    x3, y3 = test2
    pyautogui.click(x=x3, y=y3, clicks=2, interval=1)


def start():
    click('herolist.png')
    click('all.png')
    time.sleep(2)
    click('out.png')
    time.sleep(2)
    click('playhunt.png')

count = 0
while True:
    t_end = time.time() + 9000          # time for loop here (every 3 hours)
    start()
    while time.time() < t_end:
        print(count)
        print(f"{time.time()}, {t_end}")
        count += 1
        if pyautogui.locateOnScreen('newmap.png', confidence=0.9) != None:
            click('newmap.png')
            print('new map')
            continue
        if count % 1000 == 0:  ## remap because bug dern tid every 5 mins
            click('back.png')
            count = 0
            time.sleep(2)
            click('playhunt.png')
    click('back.png')
    time.sleep(3)


