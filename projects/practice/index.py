import json

items=json.loads('[{"id":1,"text":"item 1"},{"id":2,"text":"item 2"}]')

for item in items:
    print(item["id"])