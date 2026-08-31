import pandas as pd

# 샘플 데이터 생성
df = pd.DataFrame({
    "지역": ["강남구", "서초구", "송파구"],
    "거래건수": [120, 98, 145]
})

# 1) CSV 저장 (한글 깨짐 방지: encoding="utf-8-sig")
df.to_csv(
    "py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수.csv",
    index=False,               # 불필요한 행 번호 저장 안 함
    encoding="utf-8-sig"       # 엑셀에서 열었을 때 한글 깨짐 방지
)

# 2) JSON 저장 (한글 원본 유지: force_ascii=False)
# orient: records, columns(기본값), index, split, values, table
# indent: None(기본값)
df.to_json(
    "py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수.json",
    orient="columns",          # 리스트 안 딕셔너리 구조로 저장 [{col: val}, ...]
    force_ascii=False,         # 한글을 유니코드가 아닌 한글 그대로 저장
    indent=4                   # 가독성을 위한 줄바꿈/들여쓰기
)

print("\nCSV, JSON 저장 완료")