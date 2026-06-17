'''
데이터 타입
1) 기본 데이터
    - 숫자(int, float)
    - 문자(str)
    - 불(bool)
2) 복합 데이터
'''

# 숫자형(numeric) : int(정수), float(실수)
x, y, z = 10, 3.14, -5
print(type(x), type(y), type(z))

# 지수 표현식(exponential notation)
a = 17e3
b = 17E3
c = -35.2e2
d = 275e-2
print(a, b, c, d)

# 불(bool): True, False -> 논리값
# 대입(할당) 연산자: =
# 비교 연산자: > < ==
# 100이 50보다 큰가? 참
a = 100 > 50
# 100이 50보다 작은가? 참
b = 100 < 50
# 100이 50보다 같은가? 참
c = 100 == 50
print(a, b, c)
# type(): 데이터의 유형을 확인 내장 함수
type(a)

# 문자형(str): "", ''
a = "Hello"
b = '123'
c = 'How are you?'
# 다중 커서: ctrl+alt+위아래방향키 또는 alt+클릭
print(type(a))
print(type(b))
print(type(c))

# 다중 행 문자열(''', """)
x = """Twinke, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""
print(x)

y = "Twinke, twinkle, little star,\
How I wonder what you are!\
Up above the world so high,\
Like a diamond in the sky."
print(y)

# 타입 변환 함수
# int(), float(), str(), bool()
temperature = '20'
humidity = '50'
# 문자끼리는 문자열 연결
# 숫자끼리는 덧셈
print(temperature + humidity)

print(int(temperature) + int(humidity))

a = 0 # False
b = 500 # True -> 0 이외의 숫자는 모두 True
c = '' # 빈값 -> False
d = '하하호호' # True
e = None
print(bool(a), bool(b), bool(c), bool(d), bool(e))
# False True False True False