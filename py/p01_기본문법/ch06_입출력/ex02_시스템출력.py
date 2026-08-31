# 시스템 출력
# sep 매개변수: 구분자 변경
# 기본값: sep=" "
print("사과", "복숭아", "망고")
# 기본값이 있는 sep와 end는 마지막 인자로 기록한다.
# print(sep=" ", "사과", "복숭아", "망고") -> 에러
# 구분자: ,
print('사과', '복숭아', '망고', sep=',')

# end 매개변수: 줄바꿈 제어
# 기본값: end='\n'
print('이것은 문장 입니다.', end='\n')
print('문장 입니다.', end='\n')

# 줄바꿈x
print('이것은 문장 입니다.', end='')
print('문장 입니다.')

# 문자열 연결: +
# 나이: 20살
age = 20
print('나이: ' + str(age) + '살')

# 개행문자: \n
print("산토끼 토끼야\n어디를 가느냐\n깡총깡총 뛰어서\n어디를 가느냐")

# 문자열 포맷팅: 문자열.format()
'''
print('메시지: {} {}'.format(값1, 값2, ...))
print('메시지: {0} {1}'.format(값1, 값2, ...))
'''

# 기본 포맷 스트링
food = '치킨'
text = '나는 {}을 먹고 싶다'
print(text.format(food))

print('나는 {}을 먹고 싶다'.format('치킨'))

# 다중 값 치환
food1 = '피자'
food2 = '치킨'
text = '나는 {}, {}을 먹고 싶다'
print(text.format(food1, food2))

# 인덱스를 활용한 위치 지정
text = '나는 {0}, {1}을 먹고 싶다'
print(text.format(food1, food2))

text = '나는 {1}, {0}을 먹고 싶다'
print(text.format(food1, food2))

print('나는 {0} {1}을 먹고 싶다. 우리집엔 {1}이 배달되지 않아 슬프다.'.format(food1, food2))
# IndexError: Replacement index 2 out of range for positional args tuple

# 키워드를 활용: 인덱스대신 변수이름으로
text = '{name}님, 반갑습니다. 적립금은 {money}원 입니다.'
print(text.format(name = '홍길동', money = 500))

# 문자열에 %s를 작성하여, 치환할 문자를 지정
food = '치킨'
print('나는 %s을 먹고 싶다.' % food)

# 숫자 포맷팅
# 소수점 둘째자리까지 표시(반올림)
print('{:.2f}%  확신합니다.'.format(95.1234567))
print('{:.2f}%  확신합니다.'.format(95.12567))

# 천 단위마다 ,
print('한 달 휴대폰 요금은 {:,}원 입니다.'.format(100000))