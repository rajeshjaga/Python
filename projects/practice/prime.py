i = int(input("push the intger"))

for x in range(1, i):

    d = i % x
    if d == 0:
        print(x)

