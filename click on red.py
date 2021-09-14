
import pyautogui
from pynput.mouse import Button, Controller
from ctypes import windll
import win32api, win32con

from screeninfo import get_monitors


def getpixel(x, y):   # timed to take ~ 0.01s
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc, x, y), 3, "little"))


dc = windll.user32.GetDC(0)
mouse = Controller()

mouseDown = True

monitorX = 1920
monitorY = 1080

for m in get_monitors():
    if m.is_primary:
        monitorX = m.width
        monitorY = m.height

crossX = int(monitorX/2)
crossY = int(monitorY/2)+10  # Rough estimate of crosshair location

while True:  # Replace with a case for stopping program
    if mouseDown:
        color = getpixel(crossX, crossY)
        if color == (255, 0, 0):  # measure the real value for real program
            print("click")

            # Consider using an arduino to emulate a hardware click
            # pyautogui.click()  # anti cheat :(
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, crossX, crossY, 0, 0)
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, crossX, crossY, 0, 0)
            break  # remove for actual code
