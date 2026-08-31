# strip() 메서드: 앞 뒤 공백 제거
from bs4 import BeautifulSoup

html_doc = """ 
<span>\n      맨체스터 유나이티드   \n</span>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 공백이 가득한 상태
raw_text = soup.find('span').text
print(raw_text)
# 출력: "\n      맨체스터 유나이티드   \n"

# .strip()으로 양쪽 공백 및 줄바꿈 깔끔하게 청소
clean_text = raw_text.strip()
print(clean_text)
# 출력: "맨체스터 유나이티드"