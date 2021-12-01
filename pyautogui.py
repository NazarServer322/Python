import os
import pyautogui
import time
import psutil
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1.5
time.sleep(4)
x = pyautogui.position()
print(x)
pyautogui.moveTo(x=73, y=741, duration=1) # step  find search
pyautogui.click()
pyautogui.typewrite("RadiantRFID VAT Database Update Manager", interval=0.1)
pyautogui.moveTo(x=180, y=187, duration=1) # step find radiant dbupdate 
pyautogui.moveTo(x=258, y=216, duration=1) # step find radiant dbupdate  x=252, y=227
pyautogui.rightClick()
pyautogui.moveTo(x=400, y=232, duration=1) # step find radiant dbupdate  x=712, y=645
pyautogui.click()
time.sleep(10)
pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(x=400, y=232, duration=1)
pyautogui.moveTo(x=712, y=645, duration=1)
pyautogui.click()
def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


while True:
    if checkIfProcessRunning("RadiantRFID.VAT.DatabaseUpdateManager"):
        print("this running")
        time.sleep(1)
        pyautogui.moveTo(x=945, y=606, duration=1)
        pyautogui.click()
    else:
        print("fuck")
        break