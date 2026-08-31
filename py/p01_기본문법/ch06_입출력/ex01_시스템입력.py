# 시스템 입력
# input()
# 사용자로부터 터미널에 이름을 입력받는다.
'''
이름을 입력하세요: 홍길동
'''
name = input('이름을 입력하세요:')
print(name + '님, 안녕하세요.')

# 키에 따른 권장체중
# input은 항상 문자열을 반환 -> int('170') -> 170
height = input('키를 입력하세요:')
print('나의 키는 ' + height + 'cm 입니다.')
height = float(height)
weight = (height - 100) * 0.9
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
# print('당신의 권장체중은 weightkg 입니다.')
print('당신의 권장체중은 ' + str(weight) + 'kg 입니다.')
print('당신의 권장체중은 {}kg 입니다.'.format(weight))
# f-string
print(f'당신의 권장체중은 {weight}kg 입니다.')
