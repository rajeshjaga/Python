#for n in range(5):
#    print (n)
#veg
menu=['veg','Meat','fish','pork']
for n in range((len(menu))):
    print(n+1,menu[n])
me=input('Veg or Non-Veg')
ch=input('enter the number choice in menu accordingly')
print('you have chosen ',menu[ch])
men=input ('what would you like to have')
if me=='veg':

    if men=='dosa':
        print('Dosa will be available in 10 min')
    elif men!='dosa':
        print('fastfood is not available')
elif me=='non-veg':
    if men=='chicken':
        print('noveg is not available')
    else:
        print('not now its not available for ever')
