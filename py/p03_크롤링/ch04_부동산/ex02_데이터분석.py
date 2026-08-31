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
