import pyautogui
import pygetwindow
import time
from datetime import datetime
from pynput.keyboard import Controller

keyboard = Controller()

import os
filedir = os.path.dirname(os.path.abspath(__file__)) + '\\'

def screenshot(file_name):
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    active_window = pygetwindow.getActiveWindow()

    if active_window:
        left = active_window.left
        top = active_window.top
        width = active_window.width
        height = active_window.height
    else:
        left = 0
        top = 0
        width = pyautogui.size().width
        height = pyautogui.size().height

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    directory = filedir + "screenshot\\"
    if not os.path.exists(directory): os.makedirs(directory)
    file_full_path = directory + date + "_" + file_name + '.jpg'
    screenshot.save(file_full_path)
    print("Saved to " + file_full_path)


def click(button_image_path, offset_x=0, offset_y=0):
    button_location = pyautogui.locateOnScreen(filedir + button_image_path, confidence=0.8)
    if button_location:
        # Step 2: click vào textbox
        textbox_center = pyautogui.center(button_location)
        pyautogui.click(textbox_center[0] + offset_x, textbox_center[1] + offset_y)
        time.sleep(1)
        print("Clicked on " + button_image_path + " textbox.")
    else:
        print("Could not locate the " + button_image_path + " textbox.")

def focus_window():
    window = None
    for w in pygetwindow.getAllTitles():
        if "English Learning App" in w:
            window = pygetwindow.getWindowsWithTitle(w)[0]
            break

    if window:
        window.activate()
        print("Focused on: English Learning App")
    else:
        print("Could not find the 'English Learning App' window.")
        exit()

def type_in(textbox_image_path, value, offset_x=0, offset_y=0):
    textbox_location = pyautogui.locateOnScreen(filedir + textbox_image_path, confidence=0.8)

    if textbox_location:
        # Step 2: click vào textbox
        textbox_center = pyautogui.center(textbox_location)
        pyautogui.click(textbox_center[0] + offset_x, textbox_center[1] + offset_y)
        print("Clicked on " + textbox_image_path + " textbox.")

        # clear data
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.2)
        pyautogui.press('backspace')

        # Step 3: nhập data
        # pyautogui.typewrite(value, interval=0.1)
        for char in value:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.1)
    else:
        print("Could not locate the " + textbox_image_path + " textbox.")