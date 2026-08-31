# 람다(lambda)
# : 익명 함수를 한 줄로 간편하게 표현
# 방법1: 람다를 정의하는 동시에 실행
print((lambda x : x + 5)(100))

# 방법2: 람다를 변수에 할당하여 재사용
sum5 = lambda x : x + 5
print(sum5(100))

# 권장 체중 계산
# 권장 체중 = (키 - 100) * 0.9
'''
변수(함수명) = lambda 매개변수 : 실행문
'''
weight = lambda height : (height - 100) * 0.9
print(weight(170))

def weight_value(height):
    return (height - 100) * 0.9
print(weight_value(170))

print((lambda height : (height - 100) * 0.9)(170))

# 매개 변수가 2개
weight2 = lambda man, height : (height - 100) * 0.9 if (man) else (height - 100) * 0.85

print(weight2(False, 170))
print(weight2(True, 170))

# 일반 함수
def weight_value2(man, height):
    if man:
        return (height - 100) * 0.9
    else:
        return (height - 100) * 0.85