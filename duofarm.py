#!/usr/bin/env python3
# farm duolingo xp

import pyautogui as pag
import time

browser = "firefox"
url = "https://www.duolingo.com/characters"
startButtonAdress = 'media/duolingo-start.png'
waittimes = {'loadBrowser' : 0.5,
             'loadDuolingoTab' : 2,
             'loadLesson' : 1,
             'pageup' : 0.1}
press1count = 25
press2count = 25 # also counts for trailing enters


class Hotkey:
    def openProgram(program):
        pag.hotkey('win', 'd')
        pag.write(program + '\n')
        return 0


def init():
    global startButton
    #open browser
    Hotkey.openProgram(browser)
    time.sleep(waittimes['loadBrowser'])
    #open duolingo
    pag.write(url+'\n')
    time.sleep(waittimes['loadDuolingoTab'])
    #click start button
    startButton = pag.locateCenterOnScreen(startButtonAdress)
    return 0

def loop():
    pag.click(startButton)
    time.sleep(waittimes['loadLesson'])
    for i in range(press1count):
        pag.press('1')
        pag.press('enter')
        pag.press('enter')
    for x in range(1,5): #left numbers
        for y in range(5,9): #right numbers
            pag.press(str(x))
            pag.press(str(y))
    for i in range(press2count):
        pag.press('2')
        pag.press('enter')
        pag.press('enter')
    pag.keyDown('pageup')
    time.sleep(waittimes['pageup'])
    pag.keyUp('pageup')
    return 0

def main():
    init()
    while True:
        loop()

main()
