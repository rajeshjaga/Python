import sys
import os 

def_path = "c:/users/hp/documents/github/"

path=os.path.join(def_path,sys.argv[1])
print(path)
os.chdir(path)
print(os.getcwd())