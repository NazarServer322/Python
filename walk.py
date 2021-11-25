import os 
import datetime
import shutil
import glob
folder = os.chdir("C:\\PythonRMFolder")
listdir = os.listdir(".\\")
filetime = datetime.datetime.fromtimestamp(1)
for listdir in os.listdir('.\\'):
    if listdir.startswith("TEST") and listdir.day <= 1:
         shutil.rmtree(listdir)