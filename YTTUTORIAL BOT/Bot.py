from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os
#Tile 1 Position: X:  581 Y:  400 RGB: ( 77,  80, 115)
#Tile 2 Position: X:  682 Y:  400 RGB: (  0,   0,   0)
#Tile 3 Position: X:  770 Y:  400 RGB: ( 79,  82, 116)
#Tile 4 Position: X:  869 Y:  400 RGB: ( 80,  83, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
	
os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')


time.sleep(1)
click(1180, 75)
time.sleep(1)
pyautogui.typewrite('https://www.agame.com/game/magic-piano-tiles',0.1)
pyautogui.press('enter')
time.sleep(6)
click(449, 377)
time.sleep(1)
click(27, 525)
time.sleep(1)
click(600, 420)


while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(528, 400)[0] == 0:
        click(528, 350),click(528, 405)
    if pyautogui.pixel(640, 400)[0] == 0:
        click(640, 350),click(640, 405)
		
    if pyautogui.pixel(750, 400)[0] == 0:
        click(750, 350),click(750, 405)
		
    if pyautogui.pixel(818, 400)[0] == 0:
        click(818, 350),click(818, 405)
		