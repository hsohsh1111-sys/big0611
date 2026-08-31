from bs4 import BeautifulSoup as Bs

html_doc = '''
<!doctype html>
<html>
    <head>
        <title>기초 웹 크롤링</title>
    </head>
    <body>
        <table class="one">
            <caption>과일 가격</caption>
            <tr>
                <th>상품</th>
                <th>가격</th>
            </tr>
            <tr>
                <td>오렌지</td>
                <td>100</td>
            </tr>
            <tr>
                <td>사과</td>
                <td>150</td>
            </tr>
        </table>

        <table class="two">
            <caption>의류 가격</caption>
            <tr>
                <th>상품</th>
                <th>가격</th>
            </tr>
            <tr>
                <td>셔츠</td>
                <td>30000</td>
            </tr>
            <tr>
                <td>바지</td>
                <td>50000</td>
            </tr>
        </table>
    </body>
</html>
'''

soup = Bs(html_doc, 'html.parser')
# soup.find_all('태그명', 속성딕셔너리)
# soup.find_all('태그명', {'속성':'속성값'})
clothes = soup.find_all('table', {'class':'two'})
print(clothes)
