from bs4 import BeautifulSoup

html_doc = '''
<!doctype html>
<html>
    <head>
        <title>기초 웹 크롤링 따라하기</title>
    </head>
    <body>
        <div> 첫 번째 부분 </div>
        <div> 두 번째 부분 </div>
    </body>
</html>
'''

soup = BeautifulSoup(html_doc, 'html.parser')
body = soup.find('body')
# print(body)
div1 = soup.find('div')
# print(div1)
# soup.find_all('태그명') -> 리스트로 리턴
div_total = soup.find_all('div')
# print(div_total)
# [<div>첫 번째 부분</div>, <div> 두 번째 부분 </div>]
div1 = div_total[0]
div2 = div_total[1]
# print(div2)
print(div1.text)
print(div2.text)