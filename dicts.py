def personel(dictionary):
    for key,val in dictionary.items():
        print(f'I am {key} and my age is{val}')


dicts={}

while True:
    name=input('Enter your name: ')
    age=input('Enter the age : ')
    dicts[name]=age

    another=input('Do you want to enter another person name (y/n): ')
    if another=='y':
        continue
    else:
        break


count(dicts)
