import time
import psutil

def getService(name):

    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service
check = getService("HPNetworkCap")
dict = check.get("status")
while True:
    if dict == "running":
        print("exelent")
        break
    else:
        time.sleep(10)
        print("Still instaling")
    