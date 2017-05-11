import requests
import json
from bs4 import BeautifulSoup
import lxml
import codecs

res = requests.get('https://hackmd.io/s/HkbDAi51Z')
soup = BeautifulSoup(res.text, "lxml")

filename = soup.select('#doc')[0].text.split('###').replace(' ')[0]
print(filename)
content = soup.select('#doc')[0].text.split('##')

a = json.dumps(content, ensure_ascii=False)
#print (a)

file = open("content.json", "w", encoding='utf-8')

output = {"content": content}
json.dump(output,file, ensure_ascii=False)
file.close()