# 함수(function, 기능)?
# 함수 정의
'''
def 함수명([매개변수1], ...):
    실행문
    [return 값]
    실행문

들여쓰기 주의!
1. tab키
2. spacebar 4칸
3. tab과 spacebar는 섞으면x
'''
def test():
    print('함수 연습')

# 함수 호출
'''
함수명([인자1], ...)
'''
test()

# 매개변수(parameter)를 사용한 함수
def coffee(temp):
    if temp > 0:
        print("아아")
    else:
        print("핫아")

coffee(30)
# 재사용
coffee(-10)

# return 사용!
def coffee(temp):
    result = ''
    if temp > 0:
        result = '아아'
    else:
        result = '핫아'
    return result

c = coffee(30)

# + 연산자
print('추천 커피는 ' + c + '입니다.')
# 문자열.format()
print('추천 커피는 {}입니다.'.format(c))
# f-string
print(f'추천 커피는 {c}입니다.')

c = coffee(-10)
print(f'추천 커피는 {c}입니다.')

# 점수 업데이트 함수
def update_scores(scores):

    new_scores = []
    for score in scores:
        new = score + 5
        new_scores.append(new)
    
    return new_scores

scores = [80, 90, 70, 65, 85, 95, 90, 80, 75, 80]

new = update_scores(scores)
print(new)

# 여러 개의 매개변수
def get_char_count(lyric, char):
    count = 0
    for txt in lyric:
        if txt == char:
            count += 1
    return count

lyric = """산토끼 토끼야. 어디를 가느냐. 깡충깡충 뛰면서. 어디를 가느냐.
산고개 고개를. 나혼자 넘어서. 토실토실 알밤을. 주워 올 테야."""


toh = get_char_count(lyric, '토')
print(toh)
sahn = get_char_count(lyric, '산')
print(sahn)

star = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""

w = get_char_count(star, 'w')
print(w)

# 문자열.upper(): 대문자로
# 문자열.lower(): 소문자로
# return 값이 여러 개
def change_word_case(word):
    upperCase = word.upper()
    lowerCase = word.lower()
    return upperCase, lowerCase

# (a, b) = (1, 2)
# upper, lower = upperCase, lowerCase
upper, lower = change_word_case('I love Seoul.')

print('대문자는 {} 이고, 소문자는 {} 이다.'.format(upper, lower))
print('대문자는 {0} 이고, 소문자는 {1} 이다.'.format(upper, lower))
print('대문자는 {1} 이고, 소문자는 {0} 이다.'.format(upper, lower))

# 사칙연산 계산기
def calculator(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
    else:
        print('{}는 연산이 불가능합니다.'.format(operator))
    return -1

print(calculator('+', 200, 300))
print(calculator('*', 50, 7))
print(calculator('?', 89, 20))

# 디폴트(default, 기본값)인자
# : 매개변수에 초기값 지정
def print_weight(height, man=True):
    weight = 0
    if man:
        # weight = (height/100) ** 2 * 22
        weight = (height - 100) * 0.9
    else:
        weight = (height - 100) * 0.85
    print('권장 체중은 {}kg 입니다.'.format(weight))

# 입력 단위: cm
print_weight(170)
# 기본값 대신 True가 man에 전달
print_weight(170, True)
print_weight(170, False)

# 에러: 초기값이 있는 매개변수는 마지막에 기록
# def print_weight(man=True, height):
#     weight = 0
#     if man:
#         # weight = (height/100) ** 2 * 22
#         weight = (height - 100) * 0.9
#     else:
#         weight = (height - 100) * 0.85
#     print('권장 체중은 {}kg 입니다.'.format(weight))
# SyntaxError: non-default argument follows default argument

# 가변 인자(*args)
# : *args를 사용하면 개수에 제한 없이 여러 인자를 튜플 형태로 받을 수 있다.
def sum(*args):
    print(type(args)) # (1, 2, 3)
    print(args) # (1, 2, 3)
    result = 0
    for num in args:
        result += num
    return result

print(sum(1, 2, 3))
print(sum(2, 4, 6, 8, 10))

# 온도 변환 프로그램
'''
(1) 섭씨 온도를 화씨 온도로 변환
화씨 = (섭씨 x 9/5) + 32
(2) 화씨 온도는 소수점 첫째 자리까지만 출력

출력 예시
섭씨 25도는 화씨 77.0도입니다.
'''
def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환하는 함수"""
    fahrehiet = (celsius * 9/5) + 32
    return fahrehiet

celsius_temp = 33.2
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
# .2f
print(f'섭씨 {celsius_temp}도는 화씨 {fahrenheit_temp:.2f}도입니다.')