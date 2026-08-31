import csv
import json

data1 = [
    ['지역', '거래건수'],
    ['강남구', 120],
    ['서초구', 98],
    ['송파구', 145]
]

data2 = [
    {"지역": "강남구", "거래건수": 120},
    {"지역": "서초구", "거래건수": 98},
    {"지역": "송파구", "거래건수": 145}
]

# CSV 파일 저장(write)
# newline='' -> 줄바꿈을 안함 -> 두 번 줄바꿈을 한 번 줄바꿈으로
# utf-8-sig(signature)
with open("py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수6.csv", "w", newline='', encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(data1) # 전체 데이터를 한 번에 쓰기

# CSV 파일 저장2
with open("py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수6.csv", "w", newline='', encoding="utf-8-sig") as f:
    colnames = ['지역', '거래건수']
    writer = csv.DictWriter(f, fieldnames=colnames)

    writer.writeheader() # 헤러(컬럼명) 쓰기
    writer.writerows(data2) # 전체 데이터를 한 번에 쓰기

print("\nCSV 저장 완료")

# JSON 파일 저장(write)
with open("py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수6.json", "w", encoding="utf-8") as f:
    json.dump(
        data2,
        f,
        ensure_ascii=False,  # 한글 깨짐 방지 (한글 글자 그대로 저장)
        indent=4             # 보기 좋게 들여쓰기 적용
    )

print("\nJSON 저장 완료")


# CSV 파일 읽기(read)
with open("py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수6.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"지역: {row['지역']}, 거래건수: {row['거래건수']}")

# JSON 파일 읽기(read)
with open("py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수6.json", 'r', encoding="utf-8") as f:
    data = json.load(f)

print("\n===============")
print(data)
print("\n===============")
