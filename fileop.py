import os


if(os.path.exists("file.txt")):
    pass
else:
    f=open("file.txt","w+")

f.open("file.txt","w+")
 
# dir=input("Enter the project name :")
# directory=dir

# Parent_directory="c:/users/hp/documents/github/html"

# path=os.path.join(Parent_directory,directory)


# os.mkdir(path)
# f=open(f"{path}index.html","w+")

# style="style"
# stypath=os.path.join(Parent_directory,directory,style)
# if(os.path.exists(path)):
#     os.mkdir(stypath)
#     print("done")
# else:
#     print("undone")

# def_path="c:/users/hp/documents/github/html"
# os.chdir(def_path)

# cmd=os.getcwd()
# print(cmd)
