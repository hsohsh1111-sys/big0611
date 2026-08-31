# 문자열 분리 - split()
text = "나는    자랑스러운 태극기" \
"앞에 자유롭고 정의로운 대한민국의 무궁한 영광을 위하여 충성을 다할 것을 굳게 다짐합니다."
# 공백을 구분자로 하여 문장을 쪼갬
# -> 리스트로 출력
print(text.split())

#"-"을 구분자로 하여 문장을 쪼갬
text = "+82-10-1234-5678"
print(text.split('-'))
# split(sep=' ', maxsplit=-1)
# sep: 구분자
# maxsplit: 최대 구분 개수
print(text.split('-', 2))


# 불필요한 문자열 제거
# strip(['문자열']): 좌우 모두
# lstrip(['문자열']): 왼쪽만
# rstrip(['문자열']): 오른쪽만
# 문자열 생략하면 공백 제거
text = "    토실토실1 아기 돼지    "
print(text.strip())

text = "\n\n\n\n토실토실2 아기 돼지\n\n\n\n"
print(text)
print(text.strip('\n'))

text = "aaXXaaaaa토실토실 아기 돼지aaaaa"
print(text.strip('a'))

text = "ababab토실토실 아기 돼지ababab"
print(text.strip('ab'))

text = "aaabbbccccc토실토실3 아기 돼지aaabbbccccc"
print(text.strip('abc'))

# 왼쪽 지우기
text = "ssss토실토실 아기 돼지sssss"
print(text.lstrip('s'))
print(text.rstrip('s'))


# 문자열 연결
# 문자열1.join(문자열2)
text1 = '->'
text2 = ['인천', '도쿄', '뉴욕', '파리']
print(text1.join(text2))
# AttributeError: 'list' object has no attribute 'join'


# 문자열 검색
# 문자열1에서 문자열2의 첫 번째 위치(인덱스) 찾기
# 문자열1.find('문자열2')
text = "송아지송아지 얼룩송아지"
print(text.find('지'))
print(text.find('지', 3))
print(text.find('얼룩'))


# 문자열 개수 세기
# 문자열1.count('문자열2')
print(text.count('송아지'))

# 시작/끝 문자열 확인
# 있으면 True, 없으면 False
# startswith(접두사)
# endswith(접미사)
animals = ['사자', '송아지', '돼지', '사슴']
for i in animals:
    # i는 '사'로 시작했는가? True / False
    print(i.startswith('사'))

for i in animals:
    print(i.endswith('지'))


# 문자열 치환
# 문자열1에서 문자열2를 찾아 문자열3으로 변경
# 문자열1.replace('문자열2', '문자열3')
text = '강아지'
print(text.replace('강', '송'))


# 대소문자 변환
# lower(): 소문자로 변환
# upper(): 대문자로 변환
text = 'Coffee'
low = text.lower()
print(low)
print(low.upper())


# 사용자 명단 처리 시스템
'''
사용자로부터 여러 명의 이름을 입력받아 데이터를 정제하고 분석하는 프로그램을 작성하시오.
(요구사항)
1. 입력 데이터: " 오리, 이기자, 배철수다 " (앞뒤 공백 포함)
2. 데이터 정제: 앞뒤 공백 제거
3. 이름 분리: 쉼표와 공백(",")을 기준으로 이름들을 리스트로 분리
4. 결과 출력: 다음 형식으로 출력

(예상 출력)
=== 사용자 명단 처리 결과 ===
원본 데이터: ' 오리, 이기자, 배철수다 '
정제된 데이터: '오리,이기자,배철수다'
분리된 이름 목록: ['오리', '이기자', '배철수다']
1번째 사용자: 오리 (길이: 2자)
2번째 사용자: 이기자 (길이: 3자)
3번째 사용자: 배철수다 (길이: 4자)
'''

# 1. 입력 데이터: " 오리, 이기자, 배철수다 " (앞뒤 공백 포함)
user_input = " 오리, 이기자, 배철수다 "
# 2. 데이터 정제: 앞뒤 공백 제거
clean_input = user_input.strip()
# 3. 이름 분리: 쉼표와 공백(", ")을 기준으로 이름들을 리스트로 분리
names_list = clean_input.split(', ')

# 4. 결과 출력
print('=== 사용자 명단 처리 결과 ===')
print(f'원본 데이터: {user_input}')
print(f'정제된 데이터: {clean_input}')
print(f'분리된 이름 목록: {names_list}')

# 반복문
# enumerate(iterable객체, 시작인덱스)
# len('문자열'): 문자열의 길이
for i, name in enumerate(names_list, 1):
    # print(f'1번째 사용자: 오리 (길이: 2자)')
    # print(f'{1}번째 사용자: {오리} (길이: {2}자)')
    print(f'{i}번째 사용자: {name} (길이: {len(name)}자)')

# 1번째 사용자: 오리 (길이: 2자)
# 2번째 사용자: 이기자 (길이: 3자)
# 3번째 사용자: 배철수다 (길이: 4자)