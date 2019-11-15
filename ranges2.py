#import os
#import asyncio
def greeting (name,time):
    print(f'Hello {name} ,Good {time}')

name=input('Hello what is your name\n')
time=input('What is time of day\n')

greeting(name,time)
#print(os.name)#
