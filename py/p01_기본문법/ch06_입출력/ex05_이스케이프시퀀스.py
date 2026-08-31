# 이스케이프 시퀀스
# 큰따옴표 안에 큰따옴표를 넣고 싶을 때 (문법 충돌)
# ❌ SyntaxError 발생 (파이썬이 "그는 " 까지만 문자열로 인식함)
# print("그는 "안녕"이라고 말했다.")

print('그는 "안녕"이라고 말했다.')

# ⭕ 이스케이프 시퀀스(\") 사용
print("그는 \"안녕\"이라고 말했다.")
# 출력 결과: 그는 "안녕"이라고 말했다.


# 키보드로 칠 수 없는 제어 문자(\n, \t, ...) 표현
# 1. 줄바꿈(\n)과 탭(\t)
print("순위\t이름\n1등\t홍길동\n2등\t임꺽정")

# 2. 파일 경로 적을 때 백슬래시(\\) 구별
# \t가 '탭'으로 오인되는 것을 막기 위해 두 번 적어줍니다.
print("C:\\Users\\test\\Documents")
# 출력 결과: C:\Users\test\Documents

# 로우 문자열(Raw String)
# 문자열 앞에 r을 붙이면 내부의 \를 있는 그대로 문자 취급합니다.
path = r"C:\Users\test\Documents"
print(path)
# 출력 결과: C:\Users\test\Documents
# 참고: C:/Users/test/Documents