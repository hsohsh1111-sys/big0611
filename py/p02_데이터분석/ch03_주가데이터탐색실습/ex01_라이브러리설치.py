# 라이브러리 설치
# pip install yfinance

# 라이브러리 임포트

import yfinance as yf

# df = yf.download("AAPL", start="2026-01-01", end="2026-06-30")

df = yf.download("NVDA", period="1y", interval="1d", multi_level_index=False)
print(df.tail())

# 파이썬 프로그램 실행 방법
'''
1. *.py: F5 -> 터미널 실행
2. *.py: 실행할 코드 영역을 블록 설정 후 shift+Enter -> 블록 단위 실행
3. *.ipynb: shift+enter -> 주피터 노트북 실행(셀 단위 실행)
'''
