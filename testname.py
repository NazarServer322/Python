import os
import shutil

version = input("Enter dir name: ")
dir = os.chdir("C:\\")
shutil.copytree("C:\\Nametest", f"newfolder{version}")