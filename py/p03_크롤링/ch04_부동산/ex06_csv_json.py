from pathlib import Path
import pandas as pd

# 1. 저장 디렉토리 및 파일 경로 설정
target_dir = Path("py/p03_크롤링/ch04_부동산/data")
csv_path = target_dir / "서울_아파트_거래건수.csv"
xlsx_path = target_dir / "서울_아파트_거래건수.xlsx"
json_path = target_dir / "서울_아파트_거래건수.json"

# 2. 폴더가 없으면 상위 경로까지 자동 생성 (exist_ok=True로 중복 에러 방지)
target_dir.mkdir(parents=True, exist_ok=True)

# 샘플 데이터 생성
df = pd.DataFrame({
    "지역": ["강남구", "서초구", "송파구"],
    "거래건수": [120, 98, 145]
})

# 3. CSV 저장
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

# 4. Excel 저장
df.to_excel(xlsx_path, index=False)

# 5. JSON 저장
df.to_json(json_path, orient="records", force_ascii=False, indent=4)

print("CSV, Excel, JSON 저장 완료!")


# ==========================
# CSV 파일 불러오기
# ==========================
data = pd.read_csv(
    csv_path,
    encoding="utf-8-sig"
)
print("\n========================")
print(data)
print("========================")
""" 
========================
    지역  거래건수
0  강남구   120
1  서초구    98
2  송파구   145
========================
"""

# ==========================
# 엑셀 파일 불러오기
# ==========================
data = pd.read_excel(
    xlsx_path,
)

print("\n========================")
print(data)
print("========================")


# ==========================
# JSON 파일 불러오기
# ==========================
data = pd.read_json(
    json_path,
    orient="records",
    encoding="utf-8"
)

print("\n========================")
print(data)
print("========================")