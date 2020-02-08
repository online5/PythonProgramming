from os.path import *
import sys

FileName=sys.argv[1]
StringName=sys.argv[2]

if(isfile(FileName)):
    fp=open(FileName,"r").read()
    count=fp.count(StringName)
    print(type(fp))
    print(count)
