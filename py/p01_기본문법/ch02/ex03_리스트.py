# ctrl+d: 같은 텍스트 선택
fruit1 = 'apple'
fruit2 = '바나나'
fruit3 = '오렌지'

# 컨테이너 자료형
# : 리스트, 튜플, 세트, 딕셔너리
fruits = ['apple','바나나','오렌지']
print(fruits)

fruits2 = ['apple','바나나','오렌지','apple','바나나']
print(fruits2)

# 아이템 선택
# 인덱싱
# CRUD(Create, Read, Update, Delete )
print(fruits[0]) # apple
print(fruits[1]) # 바나나
print(fruits[2]) # 오렌지
print(fruits[-1]) # 오렌지
# 슬라이싱
print(fruits[1:3])

fruit_list = ['apple', 'banana', 'orange']
print(fruit_list[0])
print(fruit_list[-1])
print(fruit_list[1:3])


fruit_list[1] = 'kiwi'
print (fruit_list) 

fruit_list.insert(2, 'mango')
print (fruit_list) 

fruit_list.append('watermelon')
print (fruit_list) 

# print() 함수
# list 객체.insert() 메소드
vegetable_list = ['당근', '토마토', '양파']
fruit_list.extend(vegetable_list)
print(fruit_list)

list1 = [1, 2, 3]
list2 = ['가', '나', '다']
print (list1 + list2)

print('지우기 전:', fruit_list)
fruit_list.remove('토마토')
print('지운 후:', fruit_list)

del fruit_list[-1]
print(fruit_list)


fruit_list.sort(reverse = True)
print(fruit_list)