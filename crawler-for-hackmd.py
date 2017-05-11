import requests
import json
from bs4 import BeautifulSoup
import lxml

res = requests.get('https://hackmd.io/s/HkbDAi51Z')
soup = BeautifulSoup(res.text, "lxml")

content = soup.select('#doc')[0].text

print(content)

"""url= "http://www.alternate.nl/html/product/listing.html?navId=11622&tk=7&lk=9419"
r = requests.get(url) 
soup = BeautifulSoup(r.content)

product = Product()

g_data = soup.find_all("div", {"class": "listRow"}) 
for item in g_data: 
    try: 
        product.set_<field_name>(item.find_all("span", {"class": "name"})[0].text)
        product.set_<field_name>("span", {"class": "additional"})[0].text
        product.set_<field_name>("span", {"class": "info"})[0].text
        product.set_<field_name>("span", {"class": "info"})[1].text
        product.set_<field_name>("span", {"class": "info"})[2].text
        product.set_<field_name>("span", {"class": "price right right10"})[0].text
    except: 
        pass  

import json
file = open("filename", "w")
output = {"product1": product}
json.dump(output, file)
file.close()"""