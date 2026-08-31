import os
from dotenv import load_dotenv
import pymysql
from ex01_크롤링 import crawl_stock_data

res = crawl_stock_data()

load_dotenv()

conn = pymysql.connect(
    host=os.getenv("DB_HOST", "127.0.0.1"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_DATABASE"),
    charset="utf8"
)

# %s str
# %d digit -> int
# %f float


sql_state = '''INSERT INTO stock.daily_market(dt, item_name, item_code, price, foreign_ownership_ratio, rel_return, per, per_12m, per_ind, pbr, dividend_yield, volume, trans_price, market_capital_prefer, market_capital_common) VALUES ('%s', '%s', '%s', %d, %f, %f, %f, %f, %f, %f, %f, %d, %d, %d, %d)'''%(tuple(res))
print(sql_state)

# 1. 연결 객체 생성
db = conn.cursor()
# 2. SQL 쿼리문을 실행
db.execute(sql_state)
# 3. DB에 변경 사항 반영
conn.commit()
# 4. 연결 닫기
conn.close()