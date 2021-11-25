import psutil
import time
def checkIfProcessRunning(processName):
  
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

while True:
    if checkIfProcessRunning('Viber'):
        print('Yes a Viber process was running')
        time.sleep(60)
        break
    else:
        print('No Viber process was running')