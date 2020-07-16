import urllib



arm = input("enter any armstrong number to check\n")
sum=0
lenthArm=len(arm)
number=""
def CheckingIfArmstrong(a,b):    
    if b != str(a):
        print('this is not a armstong number')
    else:
        print('This is a armstrong number')
for a in arm :
    b=int(a)
    sum += b**lenthArm
    number +=a
    if len(number)==lenthArm:
        CheckingIfArmstrong(sum,arm)
    else:
        print("this is not a armstrong number")
    
    