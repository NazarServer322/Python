import os 
import time
import shutil

DAYS = 0.1

FOLDERS = "C:\\TestPythonDateRemove"


TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0  

nowTime = time.time()
Age = nowTime - 60*60*24*DAYS

def delete_old_files(folder):
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file) # path to file
            fileTIme = os.path.getmtime(fileName) # getmtime means when last time file used
            if fileTIme < Age:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile
                TOTAL_DELETED_FILE += 1
                print("file was delete" + str(fileName))
                os.remove(fileName)
def delete_empty_dir(folder):
    #global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        for dir in dirs:
            home = os.path.join(dir) 
           # file_time = os.path.getmtime(home)
            if home.startswith("VAT"): #and file_time < Age:
                shutil.rmtree(home)

           #sTOTAL_DELETED_DIRS =+ 1
           # print("delete empty dirs" + str(path))





###################
for folder in FOLDERS:
    #delete_old_files(folder)
    delete_empty_dir(folder)