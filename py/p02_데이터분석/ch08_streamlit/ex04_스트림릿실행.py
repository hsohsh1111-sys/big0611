import streamlit as st
import pandas as pd
import numpy as np

# app.py 파일을 만들고 이 코드를 전부 넣는다.
# requirements.txt 파일을 만들고 아래 내용을 넣는다.
# 1. 타이틀 및 텍스트 적기
st.title("나의 첫 데이터 대시보드 🚀")
st.write("Streamlit을 사용하면 파이썬만으로 웹 앱을 만들 수 있습니다.")

# 2. 사이드바에 슬라이더 위젯 추가
st.sidebar.header("설정 메뉴")
data_size = st.sidebar.slider("생성할 데이터 개수 선택", 10, 100, 50)

# 3. 데이터프레임 생성 및 웹에 표시
chart_data = pd.DataFrame(
    np.random.randn(data_size, 2),
    columns=['Sales', 'Profit']
)
st.subheader("실시간 데이터 표")
st.dataframe(chart_data) # 대화형 테이블 표시

# 4. 라인 차트 그리기
st.subheader("데이터 시각화")
st.line_chart(chart_data)

#5. 수행코드
streamlit run app.py