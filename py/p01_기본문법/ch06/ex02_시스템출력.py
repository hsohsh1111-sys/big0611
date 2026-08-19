print("apple", "peach", "mango")
print("apple", "peach", "mango", sep =",")
print("원숭이 엉덩이는 빨개 ")
print("빨가면 사과")
print("원숭이 엉덩이는 빨개 ", end="")
print("빨가면 사과")
print("나는" + " 빵을 " + "먹고싶다")
print("산토끼 토끼야\n어디를 가느냐\n깡총깡총 뛰어서\n어디를 가느냐")

food = "치킨"
text = "나는 {}을 먹고 싶다"
print(text.format(food))
print("나는 {}을 먹고 싶다".format(food))

food1 = "피자"
food2 = "치킨"
text = "나는 {}, {}을 먹고 싶다"
print(text.format("피자", "치킨"))
print("나는 {0}, {1}을 먹고 싶다. 우리집엔 {1}이 배달되지 않아 슬프다.".format(food1, food2))

text = "{name}님, 반갑습니다. 적립금은 {money}원 입니다.."
print(text.format(name = "홍길동", money = 500))

print("{:.2f}% 확신합니다.".format(95.1234567))
print("{:.3f}% 확신합니다.".format(95.1234567))
print("한 달 휴대폰 요금은 {:,}원 입니다.".format(100000))