import requests
import json
from bs4 import BeautifulSoup
import lxml

res = requests.get('https://hackmd.io/s/HkbDAi51Z')
soup = BeautifulSoup(res.text, "lxml")

content = soup.select('#doc')[0].text

print(content)

