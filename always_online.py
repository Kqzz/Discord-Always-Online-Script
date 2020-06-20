import pyautogui
import datetime
import random
from time import sleep
from ctypes import Structure, windll, c_uint, sizeof, byref

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

minutes_until_click = 2
time = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
print(time)
x = input("click enter to define pos")
pos = pyautogui.position()
while True:
    print(random.randint(0, 123123123123))
    idle_duration = get_idle_duration()
    print(idle_duration)
    if idle_duration >= 420:
        pyautogui.click(pos)
    sleep(minutes_until_click * 60)


print(get_idle_duration())
