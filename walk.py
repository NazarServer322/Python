import os
import shutil
import time 
import datetime
import sys
import psutil

with open ("\\\\ftp\\RRFID-RC\\Version\\Version.txt", 'r') as file:
    data = file.read().replace('\n', '')

supertime = (int((datetime.datetime.timestamp(datetime.datetime.now()))))
print("____________________________________________________________________________________________")
for root, dirs, files in os.walk("\\\\ftp\Releases\\VAT"):
    if root.endswith(data):
        shutil.copytree(root, f"C:\\Install\\TEST{supertime}", dirs_exist_ok=True)

    #for dirs in dirs:
     #   print("open the hell" + dirs)
#
#print("+___________________________________________________________________________________________")