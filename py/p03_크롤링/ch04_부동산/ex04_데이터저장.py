import os
from urllib.request import urlopen

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import pandas as pd

# 부동산 웹 크롤링
# pandas로 한눈에 알아보는 데이터 만들기
# API를 활용한 아파트 거래 건수 확인

# ==========================
# 공공데이터포털 인증키
# ==========================
# ctrl+. : 자동 임포트
load_dotenv()
serviceKey = os.getenv("MOLIT_SERVICE_KEY")

# ==========================
# 조회할 최근 12개월
# ==========================
MONTHS = [
    "202508",
    "202509",
    "202510",
    "202511",
    "202512",
    "202601",
    "202602",
    "202603",
    "202604",
    "202605",
    "202606",
    "202607"
]

# ==========================
# 지역명 : 법정동코드
# ==========================
REGIONS = {
    "종로구": "11110",
    "광진구": "11215",
    "관악구": "11620"
}

# ==========================
# 국토부 API
# ==========================
BASE_URL = "https://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade?"
result = []

# ==========================
# 데이터 수집
# ==========================
for region, lawd_cd in REGIONS.items():

    print(f"\n{region} 조회중...")

    for month in MONTHS:

        url = (
            BASE_URL
            + "serviceKey=" + serviceKey
            + "&LAWD_CD=" + lawd_cd
            + "&DEAL_YMD=" + month
            + "&numOfRows=1000"
        )

        try:
            html = urlopen(url).read()
            soup = BeautifulSoup(html, "xml")
            # print(soup.prettify())
            items = soup.find_all("item")
            trade_count = len(items)
            print(region, month, trade_count)
            result.append([
                region,
                month,
                trade_count
            ])
        except Exception as e:
            print(region, month, "오류 :", e)


# 크롤링 데이터를 데이터 프레임으로
# 데이터를 리스트 형태로 만들기
# ==========================
# DataFrame 생성
# ==========================
df = pd.DataFrame(
    result,
    columns=[
        "지역",
        "날짜",
        "거래건수"
    ]
)

print("\n========================")
print(df)
print("========================")


# 파이썬으로 CSV 파일 다루기
# CSV(Comma-Separated Values)란 무엇인가요?
# : 콤마로 구분한 텍스트 데이터 또는 파일
# TSV(Tab-Separated Values)

# 데이터 분석 결과를 CSV 파일로 저장
# ==========================
# CSV 저장
# ==========================
# 경로 복사(절대 주소) -> E:\\wi\\git\\big0611\\py\\p03_크롤링\\ch04_부동산\\서울_아파트_거래건수2.csv

# 상대 경로 복사 -> r'py\p03_크롤링\ch04_부동산\서울_아파트_거래건수3.csv' -> r은 raw string
# 상대 경로 복사 -> 'py\\p03_크롤링\\ch04_부동산\\서울_아파트_거래건수3.csv'
# 상대 경로 복사 -> 'py/p03_크롤링/ch04_부동산/서울_아파트_거래건수3.csv'
df.to_csv(
    "서울_아파트_거래건수.csv",
    index=False,
    encoding="utf-8-sig"
)
df.to_csv(
    "py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수3.csv",
    index=False,
    encoding="utf-8-sig"
)

# 파이썬으로 엑셀 파일 다루기
# 데이터 분석 결과를 엑셀 파일로 저장
df.to_excel('py/p03_크롤링/ch04_부동산/data/서울_아파트_거래건수3.xlsx', index=False)

print("\ncsv, xlsx 저장 완료")
