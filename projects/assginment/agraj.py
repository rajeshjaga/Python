def buses(n):
    c=[n]
    s=int(input(f'enter the average speed of bus'))
    for X in range(n):
        c=int(input('enter the bus no'))
        d=int(input(f'enter the distance of bus {X+1}'))
        print(f'the speed of the bus {X+1} {d/s}')
        d+=d
    print(d)
        
buses(5)