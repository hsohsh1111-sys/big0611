# 조건문 : if elif else
# 반복문 : for, while


scores = [80, 90, 70, 65, 55, 80, 90, 45, 50]
new_scores = []

for score in scores:
    new = score + 5
    new_scores.append(new)  

print(new_scores)


scores = [80, 90, 70, 65, 55, 100, 90, 45, 50]
new_scores = []

for score in scores:
    if score < 100:
        new = score + 5

    else:
        new = score        
    new_scores.append(new)  

print(new_scores)

new_scores2 = [s + 5 if s < 100 else s for s in scores ]
print(new_scores2)

scores = [80, 90, 70, 65, 55, 100, 90, 45, 50]
new_scores = []
score = 0

while score < len(scores):
    if scores[score] < 100:
        new = scores[score] + 5
    else:
        new = scores[score]
    new_scores.append(new)
    score = score + 1

print(new_scores)     

time = 0
while True:
    print('현재 사용량:' + str(time))
    if time < 150:
        pass

    if time >=300:
        print('[사용 중단]하루 사용 권장량에 도달 또는 초과하였습니다.')
        break
    else:
        time += 50 

Sentence = """산토끼 토끼야. 어디를 가느냐. 깡충깡충 뛰면서. 어디를 가느냐. 
산고개 고개를. 나혼자 넘어서. 토실토실 알밤을. 주워 올 테야."""
count = 0
for txt in Sentence:
    if txt == '냐':
        count = count + 1
print(count)

for num in range(9):
    print("3 * {} = {}".format(num + 1, (num+1)*3))

for num in range(1,9):
    print("3 * {} = {}".format(num + 1, (num+1)*3))  

bookmark = 0 
for day in range(20):
    print('[{}일차 공부계획]'.format(day+1))   
    for s in range(5):
        print('{}쪽 공부'.format(bookmark+s+1))  
    bookmark = bookmark + s + 1     


for dan in range(2, 10):
    print('2 * {} = {}'.format(day+1))   
    for s in range(5):
        print('{}쪽 공부'.format(bookmark+s+1))  
    Gugudan = Gugudan + 1   