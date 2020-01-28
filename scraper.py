import requests
from bs4 import BeautifulSoup



URL='https://www.amazon.in/Mi-Mix-6Gb-128Gb-Black/dp/B0795MQGR2/ref=sr_1_1?crid=1RUJDWDNJA3U5&keywords=mi+mix2&qid=1580185485&sprefix=mi+mix%2Caps%2C553&sr=8-1'


headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }


page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'html.parser')

print(soup.prettify())