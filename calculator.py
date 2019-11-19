class calc:

    def __init__(self,a,n):
        self.add=a+n
        self.subtract=a-n
        self.multiply=a*n
        self.divide=a%n

    def ad (self):
        print(f'The Result of  Addition are {self.add}')
        print(f'The Result of Difference are {self.subtract}')
        print(f'The Multiplication  are {self.multiply}')
        print(f'The Division of  are {self.divide}')

a=int(input('Enter the value of a :'))
n=int(input('Enter the value of b :'))

note=calc(a,n)
note.ad()
