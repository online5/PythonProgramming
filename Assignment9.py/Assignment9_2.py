
FileName=raw_input("Enter the file name to open ")
print("")
import os.path
from os import path

if(path.isfile(FileName)):
    print("FileExist")
    print("Reading from file")
    fp=open(FileName,"r")
    print(fp.read())
    fp.close()
else:
    print("File Dont Exist")
