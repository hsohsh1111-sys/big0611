pi = 3.141592
money = 1250000

# 1) 10칸 확보, 오른쪽 정렬하면서 소수점 2자리까지 표기
print(f"'{pi:>10.2f}'")
# 출력: '      3.14' (앞에 공백 6칸 + 3.14 총 10칸)

# 2) 15칸 확보, 오른쪽 정렬하면서 천 자릿수 콤마(,) 표기
print(f"'{money:>15,}'")
# 출력: '      1,250,000'
print('1234567890')
print("%-10s : %5d원" % ("apple", 1500))
print("%-10s : %5d원" % ("banana", 2500))
print("%-10s : %5d원" % ("mango", 12000))

path = r"C:\Users\test\Documents"
print(path)

f = open("abc1.txt", "w") # 쓰기모드로 파일 열기
f.write("A B C D E F G ")
f.close()

f = open("abc2.txt", "w")
f.write("a b c d e f g ")
f.close()

f = open("abc1.txt", "a")
f.write("H I J K L M N O P Q R S T U V W X Y Z")
f.close()

f = open('abc1.txt', 'r')
print(f.read())

with open("일기.txt", "w", encoding="utf-8") as f:
    f.write("2026년 6월 22일 월요일\n")

with open("일기.txt", "a", encoding="utf-8") as f:
    f.write("대체로 흐림")

with open("일기.txt", "r", encoding="utf-8") as f:
    print(f.read())
         