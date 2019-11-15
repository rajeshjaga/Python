#import arduino lib
#import esp
#this input is from esp module
#get get input from esp module
global led
led =int(input('Indication level leds'))
def water_level (level):
    if(level==1):
        print('start filling')
    elif(level==2):
        print('notify or ask')
    elif (level==3):
        print('button')
    elif(level>3):
        print('dont ask water is full')
    else:
        print('get the data again')

water_level(led)


print('notify android device using static ip\n')
run=int(input('what is The Duration you want to run the machine\n'))

#def true(levl):
#    if()


def override_switch(level,run):
    if(run>0):
        print('TIME IS VALID')
        if (level==1):
            print('ask if automation is reqiure')
        elif(level==2):
            print('it is half fill')
        elif(level==3):
            print('water if 3 quater filled')
        else:
            print('water is too much or device is not responding')
    else:
        print('notify the user for the worng input')
    return level
    return run
override_switch(led,run)

output_not=input('do  you want to see the water level')


def output (level,trueorfalse):
    print('the machine will run for (Min)',run)
    if(run>0):
        if(trueorfalse=='true'):
            print('DEVICE IS CONNECTED')
            if(level>0):
                print('water is available')
            elif(levels<0):
                print('no water')
            else:
                print('device not responding')
        else:
            print('device is not connected')
    else:
        print('nothing')


output(override_switch,output_not)
