# 파이썬으로 MySQL 데이터 불러오기
import os

from dotenv import load_dotenv
import pymysql

def db_select():

    # 1. .env 파일의 환경 변수 로드
    load_dotenv()

    conn = pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_DATABASE"),
        charset="utf8"
    )

    # SELECT 열이름 FROM [데이터베이스명.]테이블명 [WHERE 조건];
    sql_state = '''SELECT * FROM stock.daily_market;'''

    # 2. 연결 객체 생성
    db = conn.cursor()
    # 3. SQL 쿼리문을 실행
    db.execute(sql_state)
    # 4. DB에 변경 사항 반영
    rows = db.fetchall()
    # 5. 연결 닫기
    conn.close()

    print(rows)

    return rows