class add:

    def __init__(self,a,b):
        self.x=a
        self.y=b
        self.z=a+b

    def calc(self):
        print(f'the addition of the numbers of {self.x} and {self.y} are {self.z}')



a=int(input('Enter the value of int a '))
b=int(input('Enter the value of int b '))
res=add(a,b)
res.calc()
