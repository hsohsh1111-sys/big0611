# 첫 번째 웹 크롤링 실습
# 웹 페이지에서 소스 코드를 확인하는 법
# https://ai-dev.tistory.com/1
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://ai-dev.tistory.com/1'
html = urlopen(url)
# print(html)
# <http.client.HTTPResponse object at 0x00000276FE32F190>
# print(html.read())

# 제목과 본문 정보 웹 크롤링
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 제목 정보 크롤링
title = soup.find_all('h1')
# print(title)
# [<h1><a href="https://ai-dev.tistory.com/">인공지능 개발의 모든 것</a></h1>, <h1>크롤링의 세계에 오신 것을 환영합니다. </h1>]

# print(title[1])
# <h1>크롤링의 세계에 오신 것을 환영합니다. </h1>

# print(title[1].text)
# 크롤링의 세계에 오신 것을 환영합니다.

# 본문 정보 크롤링
contents = soup.find_all('p')
# print(contents)
# [<p>POWERED BY TISTORY</p>, <p>Hello, world!</p>, <p class="copyright">DESIGN BY <a href="#">TISTORY</a> <a class="admin" href="https://ai-dev.tistory.com/manage">관리자</a></p>, <p class="desc_g"></p>]

# print(contents[1])
# <p>Hello, world!</p>

print(contents[1].text)
# Hello, world!