import pyautogui
import cv2
import time

# """connect wallet"""
# button_locate = pyautogui.locateOnScreen('connectwallet.png', confidence=0.9)
# button_center = pyautogui.center(button_locate)
# x1, y1 = button_center
# print(button_locate)
# pyautogui.click(x=x1, y=y1, clicks=2, interval=1)
#
# """sign in matamask"""
# time.sleep(20)
# but_sign = pyautogui.locateOnScreen('sign.png', confidence=0.9)
# but_sign_cen = pyautogui.center(but_sign)
# x2, y2 = but_sign_cen
# pyautogui.click(x=x2, y=y2, clicks=1, interval=1)
#
# time.sleep(20)

def start():
    but_hero = pyautogui.locateOnScreen('herolist.png', confidence=0.9)
    but_hero_cen = pyautogui.center(but_hero)
    x3, y3 = but_hero_cen
    pyautogui.click(x=x3, y=y3, clicks=2, interval=1)

    but_work = pyautogui.locateOnScreen('work.png', confidence=0.9)
    but_work_cen = pyautogui.center(but_work)
    x5, y5 = but_work_cen
    pyautogui.scroll(-120000, x=x5, y=y5)
    pyautogui.moveTo(x5, y5+300)
    time.sleep(3)

    for i in range(14):
        pyautogui.click(button='left')
        time.sleep(0.5)

    time.sleep(2)
    but_out = pyautogui.locateOnScreen('out.png', confidence=0.9)
    but_out_cen = pyautogui.center(but_out)
    x6, y6 = but_out_cen
    pyautogui.click(x=x6, y=y6, clicks=2, interval=1)

    time.sleep(2)
    but_play = pyautogui.locateOnScreen('playhunt.png', confidence=0.9)
    but_play_cen = pyautogui.center(but_play)
    x7, y7 = but_play_cen
    pyautogui.click(x=x7, y=y7, clicks=2, interval=1)

count = 0
while True:
    t_end = time.time() + 9000          # time for loop here (every 3 hours)
    start()
    while time.time() < t_end:
        print(count)
        print(f"{time.time()}, {t_end}")
        count += 1
        if pyautogui.locateOnScreen('newmap.png', confidence=0.9) != None:
            but_newmap = pyautogui.locateOnScreen('newmap.png', confidence=0.9)
            but_mewmap_cen = pyautogui.center(but_newmap)
            x8, y8 = but_mewmap_cen
            pyautogui.click(x=x8, y=y8, clicks=2, interval=1)
            print('new map')
            continue
        if count % 300 == 0:  ## remap because bug dern tid every 5 min
            but_back = pyautogui.locateOnScreen('back.png', confidence=0.9)
            but_back_cen = pyautogui.center(but_back)
            x9, y9 = but_back_cen
            pyautogui.click(x=x9, y=y9, clicks=2, interval=1)
            count = 0
            time.sleep(2)
            but_play = pyautogui.locateOnScreen('playhunt.png', confidence=0.9)
            but_play_cen = pyautogui.center(but_play)
            x7, y7 = but_play_cen
            pyautogui.click(x=x7, y=y7, clicks=1, interval=1)
    but_back = pyautogui.locateOnScreen('back.png', confidence=0.9)
    but_back_cen = pyautogui.center(but_back)
    x9, y9 = but_back_cen
    pyautogui.click(x=x9, y=y9, clicks=2, interval=1)
    time.sleep(3)






# time.sleep(3)
# but_work = pyautogui.locateOnScreen('work.png', confidence=0.9)
# but_work_cen = pyautogui.center(but_work)
# x4, y4 = but_work_cen
# pyautogui.click(x=x4, y=y4, clicks=1, interval=1)



