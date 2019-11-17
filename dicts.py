def personel(dictionary):
    for key,val in dictionary.items():
        print(f'iam {key} and my age is{val}')


dicts={}

while True:
    name=input('Enter your name: ')
    age=input('Enter the age : ')
    dicts[name]=age

    another=input('do you want toeneter another person (y/n): ')
    if another=='y':
        continue
    else:
        break


personel(dicts)
