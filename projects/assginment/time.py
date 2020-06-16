time = input("enter time in (h:m:s)format followed by (am/pm)")
spl = time.split(":")
print("the time is")
h, m, s, mi = int(spl[0]), int(spl[1]), int(spl[2]), spl[3]
spl.pop()
if h < 1 or h > 23 or m < 0 or m > 59 or s < 0 or s > 59:
    print("provided time is incorrect")

else:
    if mi.lower() == "am" and h >= 1 and h <= 12:
        if h == 12:
            spl[0] = str(0)
        else:
            spl[0] = str(h)
    elif mi.lower() == "pm" and h >= 1 and h <= 12:
        if h == 12:
            spl[0] = str(h)
        else:
            spl[0] = str(h + 12)
    else:
        spl[0] = str(h)
    time2 = ":".join(spl)
    print(f"time is {time2}")
