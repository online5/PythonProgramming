import os.path
from os.path import *


fileName=raw_input("Enter file name to check in directory")
if(isfile(fileName)):
    print("FileExist")
else:
    print("File Dont exist")
