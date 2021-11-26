import os
import shutil
import time 
import datetime
import sys
import psutil

def getService(name):

    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service
def checkIfProcessRunning(processName):
  
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
#\\\\ftp\\RRFID-RC\\Version\\Version
#versions = input("Enter the version: ")
with open ("\\\\ftp\\RRFID-RC\\Version\\Version.txt", 'r') as file:
    data = file.read().replace('\n', '')
    #print(data)
try:
    checkDB = os.chdir("C:\\Program Files\\RadiantRFID\\VAT\\Server\\Logs\\DbUpdates")
    checkDB = os.listdir(".\\")
except Exception as notfound:
    print(notfound) 
try:   
    for check in checkDB:
        os.listdir(".\\")
    print(checkDB)
except Exception as notfound:
    print(notfound)
supertime = (int((datetime.datetime.timestamp(datetime.datetime.now()))))
x = os.chdir("\\\\ftp\Releases\\VAT\\master")

for foldername in os.listdir(".\\\\"):
    if foldername.endswith(data):
        print(str(foldername))
        shutil.copytree(foldername, f"C:\\Install\\TEST{supertime}", dirs_exist_ok=True)
    else:
         print("wrong")
         
try:
   os.system('"C:\\Program Files\\RadiantRFID\\VAT\\Server\\Uninstall.exe"' "/S") 
except Exception as err:
    print("some things wrong: " + err)
time.sleep(60)

while True:
    if checkIfProcessRunning('Un_A'):
        print('Yes a process Un_A is running')
        time.sleep(10)
    else:
        break
print('No Un_A process was running')

x = os.chdir(f"C:\\Install\\TEST{supertime}")
for newdir in os.listdir(".\\\\"):
    if  newdir.startswith("RadiantRFID_VirtualAssetTracking_Server"):
        z = os.path.join(newdir)
    else:
         print()

time.sleep(90)
print(" Start install RadiantRFID_VirtualAssetTracking_Server")
while True:
    if checkIfProcessRunning('RadiantRFID_VirtualAssetTracking_Server'):
        print('Yes a process Install RadiantRFID_VirtualAssetTracking_Server is running')
        time.sleep(15)
    else:
        break
print('Install RadiantRFID_VirtualAssetTracking_Server  process was running')
time.sleep(40)
os.system(f'"{z}"' "/S")
time.sleep(20)
databasedir = os.chdir("C:\\Program Files\\RadiantRFID\\VAT\Server\\DatabaseUpdateManager")
pats = os.path.join("C:\\Program Files\\RadiantRFID\\VAT\Server\\DatabaseUpdateManager\\RadiantRFID.VAT.DatabaseUpdateManager.exe")
os.system(f'"{pats}"' "/S")      
time.sleep(20)
print("NOW DATABASE UPDATE")
while True:
    if checkIfProcessRunning('RadiantRFID.VAT.DatabaseUpdateManager'):
        print('Yes a process Install RadiantRFID.VAT.DatabaseUpdateManager is running')
        time.sleep(15)
    else:
        break
print("last check")
time.sleep(10)
check = getService("RadiantRFID.VAT.Services")
dict = check.get("status")
while True:
    if dict == "running":
        print("The END ")
        break
    else:
        print("bad")
try:
    checkDB = os.chdir("C:\\Program Files\\RadiantRFID\\VAT\\Server\\Logs\\DbUpdates")
    checkDB = os.listdir(".\\")
    for check in checkDB:
        os.listdir(".\\")
    print(checkDB)
except Exception as wrong:
    print(wrong)