#import arduino lib
#import esp
#get input from esp module
global led
led =int(input('Indication level leds\n'))
def water_level (level):
    if(level==1):
        print('start filling\n')
    elif(level==2):
        print('notify or ask\n')
    elif (level==3):
        print('button\n')
    elif(level>3):
        print('dont ask water is full\n')
    else:
        print('get the data again\n')



def override_switch(level,run):
    print('notify android device using static ip\n')
    run=int(input('what is The Duration you want to run the machine\n'))

    if(run>0):
        print('TIME IS VALID\n')
        if (level==1):
            print('ask if automation is reqiure\n')
        elif(level==2):
            print('it is half fill\n')
        elif(level==3):
            print('water if 3 quater filled\n')
        else:
            print('water is too much or device is not responding\n')
    else:
        print('notify the user for the worng input\n')
    return level
    return run


def output (level,trueorfalse):
    print('the machine will run for (Min) :',run)
    if(run>0):
        if(trueorfalse=='true'):
            print('DEVICE IS CONNECTED\n')
            if(led>0):
                print('water is available\n')
            elif(led<0):
                print('no water\n')
            else:
                print('device not responding\n')
        else:
            print('device is not connected\n')
    else:
        print('nothing\n')

if(led>4):
    print('Please Enter th vaild led input or get the inpout led value from esp module')
    flag=1
    exit()
else:
    print('proceed')
    flag=0

print('1.Get info from esp ')
print('2.Device input ')
print('3.Get the status from esp module ')
print('4.Exit ')

def menu(inputmenu):
    if(flag==0):
        if(inputmenu==1):
            water_level(led)
        elif(inputmenu==2):
            output_not=input('do  you want to see the water level')
            override_switch(output_not)
        elif(inputmenu==3):
            output(override_switch,output_not)
        elif(inputmenu==4):
            exit()
        else:
            print('enter valid option')
    else:
        print('')
inputmenu=int(input('Enter your desired menu option'))
menu(inputmenu)
