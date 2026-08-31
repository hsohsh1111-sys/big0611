# ctrl+alt+오른쪽방향키: 창 분할
# 세트(set)
# 생성
fruit_set = {'사과', '바나나', '오렌지'}
print(fruit_set)
# 중복x
fruit_set = {'사과', '바나나', '오렌지', '사과', '바나나'}
print(fruit_set)

# 인덱싱x, 순서x
# fruit_set[1]
# TypeError: 'set' object is not subscriptable

# 추가, 순서x
fruit_set.add('키위')
print(fruit_set)

# 확장
vegetable_set = {'당근', '토마토', '양파'}
fruit_set.update(vegetable_set)
print(fruit_set)

# 삭제
fruit_set.remove('양파')
print(fruit_set)

fruit_set.clear()
print(fruit_set) # set()

del fruit_set
# print(fruit_set)