class calc:

    def __init__(self,a,n):
        self.add=a+n
        self.subtract=a-n
        self.multiply=a*n
        self.divide=a%n

    def add (self):
        print(f'The Addition of {self.a} and {self.n} are {self.add}')
        print(f'The Diffrence of {self.a} and {self.n} are {self.subtract}')
        print(f'The Multiplication of {self.a} and {self.n} are {self.multiply}')
        print(f'The Division of {self.a} and {self.n} are {self.divide}')

a=int(input('Enter the value of a :'))
n=int(input('Enter the value of b :'))

note=calc(a,n)
note.add()
