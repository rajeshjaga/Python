def area(Radius):
    return 3.14*Radius**2
def Volume(area,length):
    print(area*length)

Radius=int(input('Enter the radius of the circle :\n'))
length=int(input('Enter the Length of the circle :\n'))

area1=area(Radius)
print('The area of the cicle is ',area1)

print('The volume of the cicle is ')
Volume(area1,length)
