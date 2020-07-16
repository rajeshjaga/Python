#Identifying if the given number is armstrong number or not

ArmstrongNumber=int(input('enter the number to check\n'))

temp=ArmstrongNumber
order = len(str(ArmstrongNumber))
sum = 0

while temp>0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
    
if ArmstrongNumber == sum:
    print('this is a armstrong number')
else:
    print("this is not a armstrong number")
    
