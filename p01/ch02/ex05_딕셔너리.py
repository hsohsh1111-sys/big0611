my_dict = {
    "name":"Harry",
    "age": 27,
    "height": 190,
    "weight" : 99.9
}

print(my_dict)

my_dict.keys()
my_dict['age'] = 28
print(my_dict)

my_dict.update({'weight': 100})
print(my_dict)

my_dict.update({'address': 'Busan'})
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.pop('age')
print(my_dict)

my_dict.clear()
print(my_dict)