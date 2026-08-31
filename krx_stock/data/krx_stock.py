import os
import time
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv


# ============================================================
# 1. 기본 설정
# ============================================================

load_dotenv()

API_KEY = os.getenv("KRX_API_KEY")

if not API_KEY:
    raise ValueError("KRX_API_KEY를 찾을 수 없습니다.")

API_KEY = API_KEY.strip()

URL = "https://data-dbg.krx.co.kr/svc/apis/sto/stk_bydd_trd"

# 수집 기간
START_DATE = "2025-01-01"
END_DATE = "2026-08-26"

# 우리가 원하는 종목
TARGET_CODES = {
    "005930": "삼성전자",
    "035720": "카카오",
    "005380": "현대차",
}

# CSV 저장 위치
OUTPUT_FILE = "korean_stocks_2025_2026.csv"


# ============================================================
# 2. 하루치 데이터 가져오기
# ============================================================

def get_daily_data(date):
    """
    KRX에서 특정 날짜의 KOSPI 전체 종목 데이터를 가져온다.
    """

    params = {
        "basDd": date
    }

    headers = {
        "AUTH_KEY": API_KEY
    }

    response = requests.get(
        URL,
        params=params,
        headers=headers,
        timeout=30
    )

    if response.status_code != 200:
        print(f"  ❌ API 오류: {response.status_code}")
        print(f"  {response.text[:500]}")
        return None

    data = response.json()

    if "OutBlock_1" not in data:
        print("  ❌ 예상한 데이터 형식이 아닙니다.")
        return None

    df = pd.DataFrame(data["OutBlock_1"])

    return df


# ============================================================
# 3. 날짜별 데이터 수집
# ============================================================

def main():

    print("=" * 60)
    print("KRX 주가 데이터 수집")
    print("=" * 60)

    print(f"수집 기간 : {START_DATE} ~ {END_DATE}")
    print("대상 종목 : 삼성전자, 카카오, 현대차")
    print()

    # 날짜 생성
    dates = pd.date_range(
        start=START_DATE,
        end=END_DATE,
        freq="B"       # 평일만 생성
    )

    print(f"조회 예정 날짜 수: {len(dates)}")
    print()

    all_data = []

    for i, date in enumerate(dates, start=1):

        date_str = date.strftime("%Y%m%d")

        print(
            f"[{i}/{len(dates)}] "
            f"{date_str} 조회 중...",
            end=" "
        )

        try:

            df = get_daily_data(date_str)

            if df is None:
                print("실패")
                continue

            # 원하는 종목만 선택
            target_df = df[
                df["ISU_CD"].isin(TARGET_CODES.keys())
            ].copy()

            if target_df.empty:
                print("거래 데이터 없음")
                continue

            # 날짜 추가
            target_df["DATE"] = date_str

            all_data.append(target_df)

            print(
                f"성공 ({len(target_df)}개 종목)"
            )

        except Exception as e:

            print(f"오류: {e}")

        # API에 너무 빠르게 요청하지 않도록 잠시 대기
        time.sleep(0.2)


    # ========================================================
    # 4. 데이터 합치기
    # ========================================================

    if not all_data:

        print()
        print("❌ 수집된 데이터가 없습니다.")
        return

    result = pd.concat(
        all_data,
        ignore_index=True
    )


    # ========================================================
    # 5. 필요한 컬럼만 선택
    # ========================================================

    columns = [
        "DATE",
        "ISU_CD",
        "ISU_NM",
        "MKT_NM",
        "TDD_OPNPRC",
        "TDD_HGPRC",
        "TDD_LWPRC",
        "TDD_CLSPRC",
        "CMPPREVDD_PRC",
        "FLUC_RT",
        "ACC_TRDVOL",
        "ACC_TRDVAL",
        "MKTCAP",
        "LIST_SHRS",
    ]

    result = result[columns]


    # ========================================================
    # 6. 컬럼 이름을 알아보기 쉽게 변경
    # ========================================================

    result = result.rename(columns={
        "DATE": "date",
        "ISU_CD": "code",
        "ISU_NM": "name",
        "MKT_NM": "market",
        "TDD_OPNPRC": "open",
        "TDD_HGPRC": "high",
        "TDD_LWPRC": "low",
        "TDD_CLSPRC": "close",
        "CMPPREVDD_PRC": "change",
        "FLUC_RT": "change_rate",
        "ACC_TRDVOL": "volume",
        "ACC_TRDVAL": "trading_value",
        "MKTCAP": "market_cap",
        "LIST_SHRS": "listed_shares",
    })


    # ========================================================
    # 7. 날짜순 + 종목순 정렬
    # ========================================================

    result = result.sort_values(
        ["date", "code"]
    )


    # ========================================================
    # 8. 숫자형 데이터 변환
    # ========================================================

    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "change",
        "change_rate",
        "volume",
        "trading_value",
        "market_cap",
        "listed_shares",
    ]

    for column in numeric_columns:
        result[column] = pd.to_numeric(
            result[column],
            errors="coerce"
        )


    # ========================================================
    # 9. CSV 저장
    # ========================================================

    result.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig"
    )


    # ========================================================
    # 10. 결과 출력
    # ========================================================

    print()
    print("=" * 60)
    print("수집 완료")
    print("=" * 60)

    print(f"전체 데이터: {len(result):,}건")
    print(f"저장 파일  : {OUTPUT_FILE}")

    print()
    print("종목별 데이터 건수")

    print(
        result.groupby(
            ["code", "name"]
        ).size()
    )

    print()
    print("최근 데이터")
    print(result.tail(10))


if __name__ == "__main__":
    main()