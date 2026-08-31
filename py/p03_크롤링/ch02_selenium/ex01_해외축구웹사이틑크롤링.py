# 동적 웹 페이지 크롤링
# 스포츠 기록 사이트 접속
# https://www.livesport.com
# https://www.livesport.com/team/manchester-united/ppjDR086/
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.livesport.com/team/manchester-united/ppjDR086/'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

win01 = soup.find_all('span', {'class': 'wld wld--w'})
print(win01)
""" 
[]
"""
print(soup)