import os
import shutil
import glob

try:
    for x in range(0, 10):
        try:
            for x in range(0, 10):
                list_of_files = glob.glob(f'C:\\DeleteOldBeforInstallNEw\\*') 
                latest_file = max(list_of_files, key=os.path.getctime)
                Oldest_file = min(list_of_files, key=os.path.getctime)
                PathforLatest = os.path.join(latest_file)
                PathForOldest = os.path.join(Oldest_file)
                openfolder = os.chdir('C:\\DeleteOldBeforInstallNEw')
                listdir = os.listdir(openfolder)
        except Exception as test:
            x = x 
        try:
            for lisdir  in range(0,5):
                if PathforLatest != PathForOldest:
                    shutil.rmtree(PathForOldest)
                else:
                    x = x
        except Exception as eroor:
            x = x
except Exception as eroor:
    print("buza")