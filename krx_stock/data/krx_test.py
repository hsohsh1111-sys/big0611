import os
import requests
import pandas as pd
from dotenv import load_dotenv

# .env 읽기
load_dotenv()

api_key = os.getenv("KRX_API_KEY")

if not api_key:
    raise ValueError("KRX_API_KEY를 찾을 수 없습니다.")

api_key = api_key.strip()

# KRX API
url = "https://data-dbg.krx.co.kr/svc/apis/sto/stk_bydd_trd"

# 조회 날짜
date = "20260826"

params = {
    "basDd": date
}

headers = {
    "AUTH_KEY": api_key
}

# API 호출
response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=30
)

print("HTTP 상태 코드:", response.status_code)

# JSON 변환
data = response.json()

# 전체 데이터를 DataFrame으로 변환
df = pd.DataFrame(data["OutBlock_1"])

print("\n전체 종목 수:", len(df))

# 우리가 원하는 종목
target_codes = [
    "005930",  # 삼성전자
    "035720",  # 카카오
    "005380"   # 현대차
]

# 종목 필터링
target_df = df[df["ISU_CD"].isin(target_codes)].copy()

print("\n원하는 종목:")
print(target_df[
    [
        "ISU_CD",
        "ISU_NM",
        "TDD_OPNPRC",
        "TDD_HGPRC",
        "TDD_LWPRC",
        "TDD_CLSPRC",
        "ACC_TRDVOL",
        "ACC_TRDVAL"
    ]
])