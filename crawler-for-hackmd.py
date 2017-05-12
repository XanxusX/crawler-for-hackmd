
import requests
import json
from bs4 import BeautifulSoup
import lxml
import codecs

res = requests.get('https://hackmd.io/s/HkbDAi51Z')
soup = BeautifulSoup(res.text, "lxml")

filename = ''.join(soup.select('#doc')[0].text.split('###')[0]).replace('\n','').replace('#','')+'.json'
content = soup.select('#doc')[0].text.split('##')

for i in range(3):
    del content[0]

for c in content:
    c1 = c.split['\n\n 1']

content = [{"title": x} for x in content ]


a = json.dumps(content, ensure_ascii=False)
#print (a)

file = open(filename, "w", encoding='utf-8')

output = {0: content}
json.dump(output,file, ensure_ascii=False)
file.close()