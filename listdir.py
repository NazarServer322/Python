import os 
import shutil
import time
DAYS = 0.01
nowTime = time.time()
Age = nowTime - 60*60*24*DAYS

# dirs = os.chdir("C:\\TestPythonDateRemove")
# lists = os.listdir(dirs)
# for x in lists:
#     dirsTime = os.path.getmtime(x)
#     if x.startswith("VAT") and dirsTime < Age:
#         shutil.rmtree(x)
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
RemoveOldVAT("C:\\TestPythonDateRemove", "VAT", 0.01)