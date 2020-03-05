import os


if(os.path.exists("file.txt")):
    pass
else:
    f=open("file.txt","w+")

f.open("file.txt","w+")