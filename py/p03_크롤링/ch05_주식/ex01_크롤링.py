from datetime import date
from pydoc import source_synopsis
from turtle import st
from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib.dates import YearLocator
from seaborn import relational

url = 'https://wcomp.fnguide.com/?c_id=AA&menu_type=01&cmp_cd=005930'
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

date1 = soup.find("span", {"class":"date"})
print(date1.text) 

date2 = date1.text
date = date2.replace('[','').replace(']','').replace('/','-')
print(date) 

corp_name1 = soup.find_all('h1', {'id':'giName'})
print(corp_name1)

corp_name = corp_name1[0].text
print(corp_name)

code1 = soup.find_all('h2')[0].text
print(code1)

stock_price1 = soup.find_all('td', {'class':'cle r'})
stock_price = int(stock_price1[5].text.replace(',', ''))
print(stock_price)

tr3 = soup.find_all("tr")[2]
fgn_own_ratio = float(tr3.find("td", {"class":"cle r"}).text)
print(fgn_own_ratio)

fgn_own_ratio1 = soup.find_all("td", {"class":"cle r"})
print(fgn_own_ratio1)

rel_return1 = soup.find_all('span', {'class':'tcr'})
rel_return = rel_return1[4].text
print(rel_return)

up_list = soup.find("div", {"class":"corp_group2"})
print(up_list)
dd = up_list.find_all("dd")
print(dd)

per = float(dd[1].text)
print(per)

per_12m = float(dd[3].text)
print(per_12m)

pbr = float(dd[7].text)
print(pbr)

div_yid1 = dd[9].text
div_yid2 = div_yid1.replace('%','')
div_yid = float(div_yid2)
print(div_yid)

table1 = soup.find("div", {"id":"div1"})
table2 = table1.find_all("td")
# print(table2)

volume1 = table2[1].text
volume = int(volume1.replace(',', '').strip())
print(volume)