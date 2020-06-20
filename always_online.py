import pyautogui
import datetime
from time import sleep
from ctypes import Structure, windll, c_uint, sizeof, byref
# ------------------------------------------------------------------
# This section of code is by FogleBird on stack overflow
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

# -------------------------------------------------------------------

first_time = 0
minutes_until_click = 2
seconds_until_click = minutes_until_click * 60
time = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
print(f"the start time is {time}")
x = input("click enter to define position")
pos = pyautogui.position()
print(f"{pos} is the position that will be clicked.")
while True:
    idle_duration = get_idle_duration()
    print(f"you have been afk for {idle_duration} seconds.")
    if idle_duration >= 420:
        pyautogui.click(pos)
    if first_time <= 2:
        seconds_until_click += 1
    first_time += 1
    sleep(seconds_until_click)


print(get_idle_duration())
