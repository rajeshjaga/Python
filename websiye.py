import re


def checks(string):

    urlinks = re.findall("https*:?//\w+\.\w+\.\w+\.\w+\.", string)
    return urlinks


check = input("Enter the string")
print("Urls are :", checks(check))
