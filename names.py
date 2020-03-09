import platform


of=platform.system()


if(of=="Windows"):
    print("windows")
elif(of=="Darwin"):
    print("Macos")
elif(of=="Linux"):
    print("Linux")