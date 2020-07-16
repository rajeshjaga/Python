import os
import text as t
import main as main

#mind the branch its default is in scss-beta
def trying(cur_path):
    def_path = "c:/users/hp/documents/github/html"
    mypath = os.path.join(def_path, cur_path)
    try:
        os.chdir(mypath)
        print("the folder exists")
        ch(mypath)
    except OSError as Error:
        print("This is new project ")
        print(Error)
        print(create(mypath, cur_path))


def create(mypath, cur_path):
    os.mkdir(mypath)
    asstes = os.path.join(mypath, "assests")
    os.mkdir(asstes)
    os.chdir(mypath)
    f = open("index.html", "w+")
    stylepath = os.path.join(mypath, "style")
    os.mkdir(stylepath)
    os.chdir(stylepath)
    f2 = open("style.css", "w+")
    css = """*{
    margin:0;
    padding: 0;
    box-sizing: border-box;
}"""
    f2.write(css)
    f2.close
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style/style.css">
    <title>{}</title>
</head>
<body>
    
    <script src="./script/app.js">  </script>
</body>
</html>""".format(
        cur_path
    )
    f.write(html)
    f.close()

    sceip = os.path.join(mypath, "script")
    os.mkdir(sceip)
    os.chdir(sceip)
    f2 = open("app.js", "w+")
    if os.path.exists(mypath):
        print("done")
        os.chdir(mypath)
        os.system("code .")
        print(f"{mypath}")
    else:
        print("requests rejected")


def opion(optin):
    if optin == 1 or optin == 9:
        cre_path = input("Enter the project name :")
        print("Checking if the project exists...")
        trying(cre_path)
        if optin == 9:
            deli(cre_path)
    elif optin == 3:
        def_path = "c:/users/hp/documents/github/html"
        os.chdir(def_path)
        os.system("dir")
        cdir = input("Mention the project name to open")
        try:
            mypath = os.path.join(def_path, cdir)
            ch(mypath)
        except OSError as Error:
            print(Error)
            print(f"the project mention {cdir} doesn't exist")
            t.main(optin)
    elif optin == 2:
        cdir = input("Mention the project name (to say i don'7t recommend this option)")
        def_path = "c:/users/hp/documents/github/html"
        try:
            mypath = def_path
            os.chdir(mypath)
            print(os.getcwd())
            os.system(f"rd {cdir} /s")
        except OSError as Error:
            print(Error)
            print(f"the project mention {cdir} doesn't exist")
            t.main(optin)
    elif optin == 4:
        cdir = input("Mention the project name to archive")
        def_path = "c:/users/hp/documents/github/html"
        try:
            main.di()
        except OSError as Error:
            print(Error)
            print(f"the project mention {cdir} doesn't exist")
            t.main(optin)

    else:
        do = input("Do you want to exit ? :(Y/N)")
        if (do == "y", "Y"):
            exit()
        elif (do == "n", "N"):
            trying(cre_path)


def ch(path):
    # os.chdir(path)
    # os.system(dir)
    os.chdir(path)
    os.system("code .")


def deli(myo):
    def_path = "c:/users/hp/documents/github/html"
    mypath = os.path.join(def_path, myo)
    os.chdir(mypath)
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "initial commit"')
    print("git init done")


# input_1 = int(input("enter the option"))
# opion(input_1)
