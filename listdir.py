import os 
import shutil
import time
DAYS = 30
nowTime = time.time()
Age = nowTime - 60*60*24*DAYS

def RemoveOldVAT(Path, names, days):
    DAYS = days
    nowTime = time.time()
    Age = nowTime - 60*60*24*DAYS
    dirs = os.chdir(Path)
    lists = os.listdir(dirs)
    for x in lists:
        dirsTime = os.path.getmtime(x)
        if x.startswith(names) and dirsTime < Age:
            shutil.rmtree(x)
RemoveOldVAT("C:\\TestPythonDateRemove", "VAT", 30)