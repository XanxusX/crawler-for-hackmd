
import requests
import json
from bs4 import BeautifulSoup
import lxml

content=[]
c2=[]
'''res = requests.get('https://hackmd.io/s/HkbDAi51Z')
soup = BeautifulSoup(res.text, "lxml")

filename = ''.join(soup.select('#doc')[0].text.split('###')[0]).replace('\n','').replace('#','')+'.json'
content = soup.select('#doc')[0].text.split('##')'''
file = open('0.txt','r',encoding = 'utf-8')
data = file.read().split('##')
file.close()

for i in range(3):
    del data[0]

for d in data:
    d = d.split("\n\n")
    content.append(d)

for x in range(len(content)):
    for y in range(len(content[x])):
        if content[x] != content[0]:
            c2[x].append(content[x][y])

print(c2)
# content = [{"title": x} for x in content ]


a = json.dumps(data, ensure_ascii=False)
#print (a)

file = open('0.json', "w", encoding='utf-8')

output = {0: data}
json.dump(output,file, ensure_ascii=False)
file.close()