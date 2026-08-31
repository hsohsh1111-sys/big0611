# shift+alt+a: 다중 문자열
# alt+위아래방향키: 행 단위 위치 이동
from bs4 import BeautifulSoup

html_doc = """
<div id="content">
    안녕하세요. <span>홍길동</span>입니다.
    <p>반갑습니다!</p>
</div>
"""

# ctrl+.: 자동 임포트
soup = BeautifulSoup(html_doc, 'html.parser')
# element = soup.find('div')
""" 
    soup.find('태그명')
    soup.find('태그명', {'속성': '값'})
    soup.find('태그명', 속성='값')
    soup.find(속성='값')

    soup.find_all('태그명')
    soup.find_all('태그명', {'속성': '값'})
    # id, href, class_
    soup.find_all('태그명', 속성='값')
    soup.find_all(속성='값')
    soup.find_all(['태그명', '태그명', ...])

"""
element = soup.find(id="content")

print(element.text)
""" 
안녕하세요. 홍길동입니다.
반갑습니다!
"""
print(element.text.strip())
