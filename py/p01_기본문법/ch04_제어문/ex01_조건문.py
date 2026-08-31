# 제어문
# 조건문
'''
들여쓰기(indent)
if 조건식:
    수행문1

if 조건식:
    수행문1
else
    수행문2

조건식은 결과가 True 또는 False
비교(> < >= <= == !=), 논리(and, or, not) 연산의 결과는 True 또는 False
'''

today_temp = -30
if today_temp > 0:
    print("아이스 아메리카노")
# IndentationError: expected an indented block after 'if' statement on line 18

today_temp = -10
if today_temp > 0:
    print('아아')
else:
    print('핫아')

'''
if 조건식1:
    수행문1
elif 조건식2:
    수행문2
elif 조건식3:
    수행문2
...
else:
    수행문3
'''

today_temp = -10
if today_temp > 0:
    print('아아')
elif today_temp == 0:
    print('디아')
else:
    print('핫아')

# 중첩 if
weather = '맑음'
today_temp = 30
if weather == '맑음':
    if today_temp > 0:
        print('아아')
    elif today_temp == 0:
        print('디아')
    else:
        print('핫아')
else:
    print('먹지마!')


math_score = 80
eng_score = 100
if eng_score >= 90 and math_score >= 90:
    print('오예! 용돈 인상')
elif eng_score <= 80 and math_score <= 80:
    print('용돈 삭감 ㅠㅠ')
else: 
    print('동결')


math_score = 80
eng_score = 100
if eng_score >= 90 or math_score >= 90:
    print('오예! 용돈 인상')
elif eng_score <= 80 or math_score <= 80:
    print('용돈 삭감 ㅠㅠ')
else: 
    print('동결')