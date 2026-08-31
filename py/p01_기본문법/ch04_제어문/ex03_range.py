# range(start, stop, step)
# start: 0(default)
# step: 1

# range(stop): 매개변수가 1개일 때
# 0부터 시작해서 5 직전(4)까지 생성
# range(0, 5): 0,1,2,3,4
for i in range(5):
    print(i)

# range(start, stop): 매개변수가 2개일 때
# 2부터 시작해서 7 직전(6)까지 생성
# range(2, 7): 2,3,4,5,6
for i in range(2, 7):
    print(i)

# range(start, stop, step): 매개변수가 3개일 때
# 1부터 시작해서 10 직전까지 2씩 건너뛰며 생성 (홀수만)
# range(1, 10, 1): 1,2,3,4,5,6,7,8,9 
# range(1, 10, 2): 1,3,5,7,9
for i in range(1, 10, 2):
    print(i)

# 역순(거꾸로) 숫자 생성하기
# 5부터 시작해서 1 직전(2)까지 1씩 감소하며 생성
# range(5, 1, -1): 5,4,3,2
for i in range(5, 1, -1):
    print(i)

# print(range(5))를 하면 숫자가 안 보여요!
print(range(5))
# 출력: range(0, 5)
print(list(range(5)))
# 출력: [0, 1, 2, 3, 4]