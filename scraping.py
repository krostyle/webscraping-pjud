import requests
from bs4 import BeautifulSoup

URL='https://oficinajudicialvirtual.pjud.cl/indexN.php'
r=requests.get(URL)
soup=BeautifulSoup(r.text,'lxml')
tags=soup.body
divs=tags.find_all('div')
print((tags.contents[13]))
