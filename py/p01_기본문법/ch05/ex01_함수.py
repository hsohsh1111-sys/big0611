def test():
    print("함수 연습")
test()    
def coffee(temp):
    if temp > 0 :
        print("아이스 아메리카노")
    else:
        print("따뜻한 아메리카노")
coffee(30)  
coffee(-10)       

def update_scores(scores) :
    new_scores = []

    for s in scores:
        new = s + 5
        new_scores.append(new)
    return new_scores

scores = [80, 90, 70, 65, 85, 95, 90, 80, 75, 80]

print(update_scores(scores))

def change_word_case(word):
    upperCase = word.upper()
    lowerCase = word.lower()
    return upperCase, lowerCase

upper, lower =change_word_case('I love Seoul')
print('대문자는 {1} 이고, 소문자는 {0}이야.'.format(upper, lower))
