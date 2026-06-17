temp = 0

if temp > 0:
    print("아이스 아메리카노")
else:
    print("따뜻한 아메리카노")

#   비교 ( > < >= <= == !=)

Today_temp = 5

if Today_temp > 0:
    print('메롱')
elif Today_temp < 10:
    print('아자')
else :
    print('코피')   

weather = '맑음'
Today_temp = 5
if weather == '비':
    if Today_temp > 0:
        print('메롱')
    elif Today_temp < 10:
        print('아자')
    else :
        print('코피')  
else:
    print('먹지마!')       


math_score = 80
eng_score = 100
if eng_score >=90 or math_score >=90:
    print ('용돈 인상')
elif eng_score <=80 or math_score <=80:
    print ('용돈 삭감')
else:
    print ('동결')

