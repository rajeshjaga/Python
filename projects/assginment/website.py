import re


def find(text):
    url = re.findall("https*:?//www\.\w+\.\w+/\d+/\w+=\d+/\+/", text)
    return url


text = "https://www.flutter.dev/docs/cookbook"
print("urls :", find(text))
