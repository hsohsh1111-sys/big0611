# 딕셔너리(dict)
'''
이름 = {
    '키': 값,
    'key': value
    ...
}
'''
# 생성
my_dict = {
    'name': '헤리',
    'age': 27,
    'height': 190,
    'weight': 99.9
}

print(my_dict)

# 선택
print(my_dict.keys())
print(my_dict['age'])

# 수정(Update)
my_dict['age'] = 28
print(my_dict)

# 딕셔너리.update({키:값})
my_dict.update({'weight': 100})
print(my_dict)

# 추가
my_dict.update({'address': '부산'})
print(my_dict)

# 삭제
# 딕셔너리.popitem(): 마지막 아이템 삭제
my_dict.popitem()
print(my_dict)

# 딕셔너리.pop(키)
my_dict.pop('age')
print(my_dict)

# 딕셔너리.clear()
my_dict.clear()
print(my_dict)

del my_dict
# print(my_dict)