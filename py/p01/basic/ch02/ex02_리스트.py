# ctrl+d: 같은 텍스트 선택
fruit1 = '사과'
fruit2 = '바나나'
fruit3 = '오렌지'

# 컨테이너 자료형
# : 리스트, 튜플, 세트, 딕셔너리
fruits = ['사과','바나나','오렌지']
print(fruits)

fruits2 = ['사과','바나나','오렌지','사과','바나나']
print(fruits2)

# 아이템 선택
# 인덱싱
print(fruits[0]) # 사과
print(fruits[1]) # 바나나
print(fruits[2]) # 오렌지
print(fruits[-1]) # 오렌지
# 슬라이싱
print(fruits[1:3])