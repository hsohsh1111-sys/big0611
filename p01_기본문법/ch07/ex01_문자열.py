text = "나는 자랑스러운 태극기 앞에 자유롭고 정의로운 대한민국의 무궁한 영광을 위하여 충성을 다할 것을 굳게 다짐합니다."
print(text.split(" "))
text = "+82-10-1234-5678"
print(text.split("-"))
print(text.split("-", 2))

text = "     토실토실 아기 돼지    "
print(text.strip())

text = "\n\n\n\n토실토실 아기 돼지\n\n\n\n"
print(text.strip("\n"))

text = "XXaaaaa토실토실 아기 돼지aaaaa"
print(text.strip("a"))

text = "ababab토실토실 아기 돼지ababab"
print(text.strip("ab"))

text = "aaabbbaa토실토실 아기 돼지aaaaa"
print(text.strip("ab"))

animals = ['강아지', '송아지', '돼지']

for i in animals:
    print(i.startswith('강'))

animals = ['강아지', '송아지', '돼지']

for i in animals:
    print(i.endswith('지'))    


(예상 출력)
=== 사용자 명단 처리 결과 ===
원본 데이터: ' 한오리, 이기자, 배철수 '
정제된 데이터: '한오리,이기자,배철수'
분리된 이름 목록: ['한오리', '이기자', '배철수']
1번째 사용자: 한오리 (길이: 3자)
2번째 사용자: 이기자 (길이: 3자)
3번째 사용자: 배철수 (길이: 3자)

user_input = " 오리, 이기자, 배철수다 "
clean_input = user_input.strip()
name_list = clean_input.split(', ')



