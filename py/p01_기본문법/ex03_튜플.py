fruit_tuple = ('apple', 'banana', 'orange')
print(fruit_tuple)
fruit_tuple = ('apple', 'banana', 'orange', 'apple', 'banana')
print(fruit_tuple)
print(fruit_tuple[1])

fruit_list = list(fruit_tuple)
fruit_list.append('watermelon')
fruit_list.remove('apple')
fruit_list[1] = 'kiwi'
print(fruit_tuple)