import requests

response=requests.get("https://randomuser.me/api")
fi=open('loadedResponse.json','w+')
fi.write(response)