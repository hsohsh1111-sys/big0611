# 두 번째 웹 크롤링 실습
# 테이블과 목록 정보 크롤링
# https://ai-dev.tistory.com/2

# 테이블 정보 크롤링
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://ai-dev.tistory.com/2'
html = urlopen(url)
# print(html.read())

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 방법1 - <table> 태그 이용
table_tag = soup.find_all('table')
# print(table_tag)
# print(table_tag[0])

table_tag01 = table_tag[0].find_all('td')
# print(table_tag01)
'''
[<td style="width: 33.3333%; text-align: center;">상품</td>, <td style="width: 33.3333%; text-align: center;">색상</td>, <td style="width: 33.3333%; text-align: center;">가격</td>, <td style="width: 33.3333%; text-align: center;">셔츠1</td>, <td style="width: 33.3333%; text-align: center;">빨강</td>, <td style="width: 33.3333%; text-align: center;">20000</td>, <td style="width: 33.3333%; text-align: center;">셔츠2</td>, <td style="width: 33.3333%; text-align: center;">파랑</td>, <td style="width: 33.3333%; text-align: center;">19000</td>, <td style="width: 33.3333%; text-align: center;">셔츠3</td>, <td style="width: 33.3333%; text-align: center;">초록</td>, <td style="width: 33.3333%; text-align: center;">18000</td>, <td style="width: 33.3333%; text-align: center;">바지1</td>, <td style="width: 33.3333%; text-align: center;">검정</td>, <td style="width: 33.3333%; text-align: center;">50000</td>, <td style="width: 33.3333%; text-align: center;">바지2</td>, <td style="width: 33.3333%; text-align: center;">파랑</td>, <td style="width: 33.3333%; text-align: center;">51000</td>]
'''
'''
    for idx, ele in 리스트|튜플|딕셔너리|세트|range():
        print(idx, ele.text)
'''
# for ele in table_tag01:
#     print(ele.text)

# for idx, ele in enumerate(table_tag01):
#     print(idx, ele.text)

'''
0 상품
1 색상
2 가격
3 셔츠1
4 빨강
5 20000
6 셔츠2
7 파랑
8 19000
9 셔츠3
10 초록
11 18000
12 바지1
13 검정
14 50000
15 바지2
16 파랑
17 51000
'''

# 목록 정보 크롤링
com_list = soup.find_all('li')
# print(com_list)

'''
[<li class=""><a class="link_tit" href="/category"> 분류 전체보기 <span class="c_cnt">(2)</span> </a>
<ul class="category_list"><li class=""><a class="link_item" href="/category/%ED%81%AC%EB%A1%A4%EB%A7%81"> 크롤링 <span class="c_cnt">(2)</span> </a></li>
</ul>
</li>, <li class=""><a class="link_item" href="/category/%ED%81%AC%EB%A1%A4%EB%A7%81"> 크롤링 <span class="c_cnt">(2)</span> </a></li>, <li>모니터</li>, <li>CPU</li>, <li>메모리</li>, <li>그래픽카드</li>, <li>하드디스크</li>, <li>키보드</li>, <li>마우스</li>, <li>
<a href="/1?category=836119">
<span class="thum">
</span>
<span class="title">크롤링의 세계에 오신 것을 환영합니다.</span>
</a>
</li>]
'''

""" 
    list-style-type: disc|circle|square;
"""
com_list01 = soup.find_all('ul', {'style': 'list-style-type: disc;'})
# print(com_list01)
""" 
[<ul data-ke-list-type="disc" style="list-style-type: disc;">
<li>모니터</li>
<li>CPU</li>
<li>메모리</li>
<li>그래픽카드</li>
<li>하드디스크</li>
<li>키보드</li>
<li>마우스</li>
</ul>]
"""

com_list02 = com_list01[0].find_all('li')

for idx, ele in enumerate(com_list02):
    print(idx, ele.text)
""" 
0 모니터
1 CPU
2 메모리
3 그래픽카드
4 하드디스크
5 키보드
6 마우스
"""