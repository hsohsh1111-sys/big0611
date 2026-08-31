from bs4 import BeautifulSoup

html_doc = '''
<!doctype html>
<html>
    <head>
        <title>기초 웹 크롤링</title>
    </head>
    <body>
        크롤링을 해봅시다.
    </body>
</html>
'''

# BeautifulSoup(텍스트, '파서종류')
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)
# soup.find('태그명')
head = soup.find('head')
# print(head)
body = soup.find('body')
print(body)