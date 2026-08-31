import os
import time
from urllib.request import urlopen

from dotenv import load_dotenv
from bs4 import BeautifulSoup
import pymysql
import requests

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 토큰과 채널 가져오기
token = os.getenv("SLACK_BOT_TOKEN")
channel = os.getenv("SLACK_CHANNEL", "#general")


def stock_crawling(item):
    url = f'https://wcomp.fnguide.com/?c_id=AA&menu_type=01&cmp_cd={item}'
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser")

    # 날짜
    date1 = bs_obj.find("span", {"class":"date"})
    date2 = date1.text
    date = date2.replace('[','').replace(']','').replace('/','-')

    # 종목 이름
    corp_name1 = bs_obj.find_all("h1", {"id":"giName"})

    # text 속성: 태그 내의 텍스트를 가져오기
    corp_name = corp_name1[0].text

    # 종목 코드
    code1 = bs_obj.find_all("div", {"class":"corp_group1"})
    code2 = code1[0].find("h2")
    code = code2.text

    # 주가
    stock_price1 = bs_obj.find("tr", {"class":"rwf"})
    # 1. r 클래스를 가진 td 태그를 먼저 찾습니다.
    td_tag = stock_price1.find("td", {"class": "r"})

    # 2. td 태그 바로 아래에 있는 첫 번째 텍스트 노드를 추출하고, 공백과 ',', '/'를 제거합니다.
    stock_price1 = td_tag.find(string=True).replace('/', '').replace(',', '').strip()
    stock_price = int(stock_price1)

    # 외국인 보유 비중
    tr3 = bs_obj.find_all("tr")[2]
    fgn_own_ratio = float(tr3.find("td", {"class":"cle r"}).text)

    # 1Y 수익률
    # rel_return = float(tr3.find_all("span", {"class":"tcr"})[2].text)

    rel_return1 = bs_obj.find_all('span', {'class':'tcr'})
    rel_return2 = rel_return1[2].text.replace('+','')
    rel_return = float(rel_return2)

    # 상단 테이블 웹 크롤링
    up_list = bs_obj.find("div", {"class":"corp_group2"})
    ul = up_list.find_all("ul")

    # PER(Price Earning Ratio, 주가수익비율)
    per = float(ul[0].find_all("li")[1].text)

    # 12M PER: 12개월 뒤의 예상 주가수익비율
    per_12m = float(ul[1].find_all("li")[1].text)

    # 업종 PER
    # per_ind = float(ul[2].find_all("li")[1].text)

    raw_text = up_list.find_all('li')[5].text.strip()

    if raw_text and raw_text != '-':
        per_ind = float(up_list.find_all('li')[5].text)
    else:
        per_ind = 0.0

    # PBR(Price to Book Ratio, 주가순자산비율)
    pbr = float(ul[3].find_all("li")[1].text)

    # 배당수익률
    div_yid1 = ul[4].find_all("li")[1].text
    div_yid2 = div_yid1.replace('%','')
    div_yid = float(div_yid2)

    # 시세현황 테이블 웹 크롤링
    table1 = bs_obj.find("div", {"id":"div1"})
    table2 = table1.find_all("td")

    # 거래량
    volume1 = table2[1].text
    volume = int(volume1.replace(',', '').strip())

    # 거래대금
    trans_price1 = table2[3].text
    trans_price = int(trans_price1.replace(',', '').strip())

    # 시가총액(우선주 포함)
    mk_cpt_pfr1 = table2[6].text
    mk_cpt_pfr = int(mk_cpt_pfr1.replace(',', '').strip())

    # 시가총액(보통주)
    mk_cpt_cm1 = table2[8].text
    mk_cpt_cm = int(mk_cpt_cm1.replace(',', '').strip())


    # 결과 모음
    res = [date, corp_name, code, stock_price, fgn_own_ratio, rel_return, per, per_12m, per_ind, pbr, div_yid, volume, trans_price, mk_cpt_pfr, mk_cpt_cm]
    
    return res


def db_insert(res):
    load_dotenv()

    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_DATABASE"),
            charset="utf8"
        )

        # 데이터 삽입
        # INSERT INTO 데이터베이스명.테이블명(테이블 열 이름) VALUES(삽입하고 싶은 자료형);

        sql_state = '''INSERT INTO stock.daily_market(dt, item_name, item_code, price, foreign_ownership_ratio, rel_return, per, per_12m, per_ind, pbr, dividend_yield, volume, trans_price, market_capital_prefer, market_capital_common) VALUES ('%s', '%s', '%s', %d, %f, %f, %f, %f, %f, %f, %f, %d, %d, %d, %d)'''%(tuple(res))
        print(sql_state)

        # 1. 연결 객체 생성
        db = conn.cursor()
        # 2. SQL 쿼리문을 실행
        db.execute(sql_state)
        # 3. DB에 변경 사항 반영
        conn.commit()
    except:
        text = "Check your stock crawler."

        requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": text})        
    finally:
        # 4. 연결 닫기
        conn.close()

if __name__ == '__main__':

    item_list = ['005930', '000660', '066570']
    
    for item in item_list:
        res = stock_crawling(item)
        db_insert(res)
        time.sleep(3)