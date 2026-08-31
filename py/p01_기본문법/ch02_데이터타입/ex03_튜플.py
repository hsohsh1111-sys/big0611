# 튜플(tuple)
# 생성
fruit_tuple = ('사과', '바나나', '오렌지')
print(fruit_tuple)
# shift+alt+위아래방향키: 복제
# alt+위아래방향키: 위치 이동
fruit_tuple = ('사과', '바나나', '오렌지', '사과', '바나나')
print(fruit_tuple)

# 선택
# 인덱싱
print(fruit_tuple[1])

# 수정(Update)x
# fruit_tuple[1] = '키위'
# TypeError: 'tuple' object does not support item assignment

# 추가x
# fruit_tuple.append('수박')
# AttributeError: 'tuple' object has no attribute 'append'

# 삭제x
# fruit_tuple.remove('사과')
# AttributeError: 'tuple' object has no attribute 'remove'
# fruit_tuple.clear()

fruit_tuple = ('사과', '바나나', '오렌지', '사과', '바나나')
del fruit_tuple

fruit_tuple = ('사과', '바나나', '오렌지', '사과', '바나나')
# 타입 변환 함수
# 기본: int(), float(), str(), bool()
# 컨테이너: list(), tuple(), set(), dict()
print('29:', fruit_tuple)
# 튜플을 리스트로 변환
fruit_list = list(fruit_tuple)
fruit_list.append('수박')
fruit_list.remove('사과')
fruit_list[1] = '키위'
print('34:', fruit_list)
# 리스트를 튜플로 변환
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)