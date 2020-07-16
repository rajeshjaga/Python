#check for flutter installed or ask for the directory and if 
#its not there download flutter 


import os 
import sys


yes=["yes","y","Y","Yes","YES"]
inputPath =input("please enter the path if flutter is installed ")
def Askfordownload():
    choice=input("You don't have fluter do you want to download and install")    
    if choice  in yes:
        print("download initiated")        
    else:
        print("hello")

def check(path):
    try :
        os.chdir(path)
        print(os.getcwd())
    except OSError as error:
        print(error)
        Askfordownload()


check(inputPath)







