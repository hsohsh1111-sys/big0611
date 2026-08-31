import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# 동적 웹 크롤링
# selenium(v4.46.0)으로 실습하기
# 구글 크롬 브라우저: chrome://version/
# 버전 151.0.7922.76(공식 빌드) (64비트)
# https://sites.google.com/a/chromium.org/chromedriver/downloads -> 접속x
# https://googlechromelabs.github.io/chrome-for-testing/
# E:\wi\git\big0611\py\p03_크롤링\ch02_selenium
# E:\wi\dev0611\chromedriver-win64

# 셀레니움 3.x 이전
# 드라이버에 속한 경로에 한글명이 없어야 한다.
# driver = webdriver.Chrome('E:\\wi\\git\\big0611\\py\\p03_크롤링\\ch02_selenium\\chromedriver.exe')
# driver = webdriver.Chrome('E:/wi/dev0611/chromedriver-win64/chromedriver.exe')

# 셀레니움 4.x 이후
# 1. 회사에서 인터넷이 차단되어 있어 Selenium Manager가 드라이버를 다운로드할 수 없는 경우
# 2. Chrome(Stable, Beta, Dev)이 여러 개 설치되어 그 브라우저에 맞는 드라이버를 Service로 지정하는 경우
# service = Service('E:\\wi\\git\\big0611\\py\\p03_크롤링\\ch02_selenium\\chromedriver.exe')

# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

driver.implicitly_wait(3) # 3초 기다림
driver.get('https://www.livesport.com/team/manchester-united/ppjDR086')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
# print(soup)

# 승패 기록 페이지 크롤링하고 분석하기
# 승
win = soup.find_all('button', {'title': 'Win'})
# 무
tie = soup.find_all('button', {'title': 'Tie'})
# 패
loss = soup.find_all('button', {'title': 'Loss'})
print(f"{len(win)}승 : {len(tie)}무 : {len(loss)}패")

""" 
7승 : 1무 : 2패
"""

report = {
    'win': len(win),
    'tie': len(tie),
    'loss': len(loss)
}
print(report)
# {'win': 7, 'tie': 1, 'loss': 2}

# 딕셔너리.values()
# 딕셔너리.keys()
# 딕셔너리.items()
max_n = max(report.values())
print(report.keys())
# dict_keys(['win', 'tie', 'loss'])

for key in report:
    if (report[key] == max_n):
        print(f"맨체스터 유나이티드 팀은 최근 10 경기에서 {key}하는 경우가 많았습니다.")

# 맨체스터 유나이티드 팀은 최근 10 경기에서 win하는 경우가 많았습니다.






time.sleep(2) # 2초간 멈춤
driver.quit() # 크롬 브라우저 종료 -> 지금은 자동 종료