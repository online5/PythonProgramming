# to copy the contents of one file to another


import sys


newName=sys.argv[1]


with open("xyz.txt") as fp1:
    with open(newName,"w") as fp2:
        for line in fp1:
            fp2.write(line)
