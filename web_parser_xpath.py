# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:49:02 2020

@author: Talha
"""

import requests
from lxml import html

'''
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)
tree = html.fromstring(page.content)

biodata_table = tree.xpath('/html/body/table[3]')
#table1 = tree.xpath('')
#table2 = tree.xpath()
/html/body/table[3]/tbody/tr/td[1]/span

medalTotals={}
for name in biodata_table:
    if name not in medalTotals:
        medalTotals[name]=medalTotals[name]+1
    else:
        medalTotals[name]=1
        


import requests
from bs4 import BeautifulSoup

URL = 'https://insideri.com/1636282_000120919120026662_0001209191-20-026662'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
results = soup.find_all('table')
table = soup.find(text="Table I").find_parent("table")


import requests
from bs4 import BeautifulSoup as BS

url = 'https://insideri.com/1636282_000120919120026662_0001209191-20-026662'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)
print (BS(page.content, 'lxml'))

'''