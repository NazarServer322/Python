import os 
import shutil

dir = os.chdir("C:\\Version")
dirLS = os.listdir(dir)

with open ("C:\\version\\Version.txt", 'r') as file:
    data = file.read().replace('\n', '')
    print(data)

