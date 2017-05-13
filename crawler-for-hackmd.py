
import requests
import json
from bs4 import BeautifulSoup
import lxml

#0 added a blank space for last two question
content=[]
'''res = requests.get('https://hackmd.io/s/HkbDAi51Z')
soup = BeautifulSoup(res.text, "lxml")
content = soup.select('#doc')[0].text.split('##')'''
file = open('0.txt','r',encoding = 'utf-8')
data = file.read().split('##')
file.close()

for i in range(3):
    del data[0]

for d in data:
    d = d.split("\n\n",1)
    content.append(d)

content = [{"title": x[0], "content": x[1]} for x in content ]
a = json.dumps(data, ensure_ascii=False)
file = open('0.json', "w", encoding='utf-8')
json.dump(content,file, ensure_ascii=False)
file.close()

#1
content = []
res = requests.get('https://hackmd.io/s/Bk1agh9J-')
soup = BeautifulSoup(res.text, "lxml")
data = soup.select('#doc')[0].text.split('##')
del data[0]

for d in data:
    d = d.split("\n\n",1)
    content.append(d)

content[-1][1] = content[-1][1].split("-----")[0]
content = [{"title": x[0], "content": x[1]} for x in content ]
a = json.dumps(data, ensure_ascii=False)
file = open('1.json', "w", encoding='utf-8')
json.dump(content,file, ensure_ascii=False)
file.close()

#2
content = []
res = requests.get('https://hackmd.io/s/SJ_eW2ckW')
soup = BeautifulSoup(res.text, "lxml")
data = soup.select('#doc')[0].text.split('##')
del data[0]

for d in data:
    d = d.split("\n\n",1)
    content.append(d)

content[-1][1] = content[-1][1].split("-----")[0]
content = [{"title": x[0], "content": x[1]} for x in content ]
a = json.dumps(data, ensure_ascii=False)
file = open('2.json', "w", encoding='utf-8')
json.dump(content,file, ensure_ascii=False)
file.close()

#3
content = []
res = requests.get('https://hackmd.io/s/BkMVZn9kZ')
soup = BeautifulSoup(res.text, "lxml")
data = soup.select('#doc')[0].text.split('##')
del data[0]

for d in data:
    d = d.split("\n\n",1)
    content.append(d)

content[-1][1] = content[-1][1].split("-----")[0]
content = [{"title": x[0], "content": x[1]} for x in content ]
a = json.dumps(data, ensure_ascii=False)
file = open('3.json', "w", encoding='utf-8')
json.dump(content,file, ensure_ascii=False)
file.close()

#4
content = []
res = requests.get('https://hackmd.io/s/SJcOZ3ckb#')
soup = BeautifulSoup(res.text, "lxml")
data = soup.select('#doc')[0].text.split('##')
del data[0]

for d in data:
    d = d.split("\n\n",1)
    content.append(d)

content[-1][1] = content[-1][1].split("-----")[0]
content = [{"title": x[0], "content": x[1]} for x in content ]
a = json.dumps(data, ensure_ascii=False)
file = open('4.json', "w", encoding='utf-8')
json.dump(content,file, ensure_ascii=False)
file.close()

#5
content = []
res = requests.get('https://hackmd.io/s/SyL0b2qJW')
soup = BeautifulSoup(res.text, "lxml")
data = soup.select('#doc')[0].text.split('##')
del data[0]

for d in data:
    d = d.split("\n\n",1)
    content.append(d)

content[-1][1] = content[-1][1].split("-----")[0]
content = [{"title": x[0], "content": x[1]} for x in content ]
a = json.dumps(data, ensure_ascii=False)
file = open('5.json', "w", encoding='utf-8')
json.dump(content,file, ensure_ascii=False)
file.close()