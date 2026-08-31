# 데이터 표시와 시각화
## 데이터프레임과 테이블 표시
# 1. 데이터를 표로 보여주기
from datetime import datetime, timedelta

import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 학생 성적 데이터 만들기
data = {
    '이름': ['홍길동', '김길동', '박기흥', '이미금'],
    '수학': [85, 92, 78, 86],
    '영어': [88, 85, 90, 93],
    '과학': [90, 88, 85, 89]
}

# 데이터 분석
df = pd.DataFrame(data)

# 웹 브라우저 표시할 콘텐츠
st.title('학생 성적 데이터 표시하기')
st.dataframe(df)

# 2. 표 스타일링하기
# 온라인 쇼핑몰 판매 데이터
sales_data = {
    '상품명': ['노트북', '마우스', '키보드', '모니터', '헤드셋'],
    '가격': [1200000, 25000, 80000, 350000, 150000],
    '판매량': [15, 120, 85, 30, 45],
    '평점': [4.5, 4.2, 4.7, 4.1, 4.6]
}

df = pd.DataFrame(sales_data)

# 평점에 따라 색깔 적용
def color_rating(val):
    if val >= 4.5:
        color = 'green'
    elif val >= 4.0:
        color = 'orange'
    else:
        color = 'red'
    return f'color: {color}'

# 스타일 적용해서 표시
# Pandas 2.1.0 버전부터 applymap() -> map()
# 현재 버전: Pandas 3.0.3
# 확인: pip show pandas
styled_df = df.style.format({
    '가격': '{:,}원',
    '판매량': '{:,}개',
    '평점': '{:.1f}점'
}).map(color_rating, subset=['평점'])

st.dataframe(styled_df)

# 3. 정적 테이블 만들기
# 날씨 정보 표시용 정적 테이블
weather_data = {
    '항목': ['최고 기온', '최저 기온', '습도', '강수 확률'],
    '값': ['28°C', '18°C', '65%', '30%']
}

# 데이터 분석
weather_df = pd.DataFrame(weather_data)
st.table(weather_df)


# 기본 차트 컴포넌트
# 1. 선 그래프로 추세 보기
# 웹사이트 방문자 수 데이터 만들기
dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
visitors = np.random.randint(100, 500, 30)

# 데이터 분석
visitor_df = pd.DataFrame({
    'Date': dates,
    'Visitors': visitors
})

# 콘텐츠 구성
st.title('기본 차트 예시')
st.subheader('웹 사이트 일일 방문자 수')

st.line_chart(visitor_df.set_index('Date')['Visitors'])
# streamlit v1.13.0 이상
# pip show streamlit
# 현재 버전: 1.59.2
st.line_chart(data=visitor_df, x='Date', y='Visitors')

# 2. 막대 그래프로 비교하기
# 도시별 인구 비교
population_data = {
    '서울': 9720000,
    '부산': 3390000,
    '인천': 2950000,
    '대구': 2410000,
    '대전': 1490000
}

# 데이터 분석
population_df = pd.DataFrame(list(population_data.items()), columns=['도시', '인구수'])
print(population_df)

# 콘텐츠 구성
st.subheader('주요 도시 인구 비교')
st.bar_chart(population_df.set_index('도시')['인구수'])
st.bar_chart(data=population_df, x='도시', y='인구수')

# 3. 영역 차트로 누적 보기
'''
- 시간에 따른 여러 요소의 변화를 함께 보여줄 때는 영역 차트를 사용한다.
'''
# 월별 매출 구성 비교
monthly_data = pd.DataFrame({
    'Date': dates,
    '온라인_매출': np.random.randint(50, 150, 30),
    '오프라인_매출': np.random.randint(80, 200, 30),
    '모바일_매출': np.random.randint(30, 100, 30)
})

st.subheader('채널별 매출 구성 변화')
st.area_chart(monthly_data.set_index('Date'))
st.area_chart(data=monthly_data, x='Date')

# plotly 차트 통합
# 1. 인터랙티브 차트의 장점

st.title('Plotly 차트 통합')
dates = [datetime.now() - timedelta(days=x) for x in range(100, 0, -1)]
np.random.seed(42)
sales = np.random.randint(50, 200, 100)

# Plotly 선 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=dates,
    y=sales,
    mode='lines',
    name='일일 판매량', # 툴팁 또는 범례
    line=dict(color='blue', width=2)
))

fig.update_layout(
    title='인터랙티브 판매량 차트',
    xaxis_title='날짜',
    yaxis_title='판매량 (개)',
    height=400
)
# use_container_width=True: 화면 크기에 맞춰 차트 크기가 조정
st.plotly_chart(fig, use_container_width=True)

# 2. 산점도 차트 만들기
# 광고비와 매출의 관계
np.random.seed(42)
# 광고비
ad_spend = np.random.randint(10, 100, 50)
# 매출
revenue = ad_spend * 2.5 + np.random.normal(0, 20, 50)

scatter_fig = go.Figure()
scatter_fig.add_trace(go.Scatter(
    x=ad_spend,
    y=revenue,
    mode='markers',
    name='데이터 포인트',
    marker=dict(
        size=8,
        color='lightblue',
        line=dict(width=1, color='navy')
    )
))

scatter_fig.update_layout(
    title='광고비 vs 매출 관계',
    xaxis_title='광고비 (만원)',
    yaxis_title='매출 (만원)',
    height=400
)

st.subheader('산점도 차트')
st.plotly_chart(scatter_fig, use_container_width=True)


# 3. 파이 차트로 비율 보기
'''
- 전체에서 각 부분이 차지하는 비율을 보여줄 때는 파이 차트를 사용한다.
- 파이 차트는 전체 100%에서 각 항목이 차지하는 비율을 직관적으로 보여준다.'''
# 설문조사 결과
survey_data = {
    '매우 만족': 25,
    '만족': 40,
    '보통': 20,
    '불만족': 10,
    '매우 불만족': 5
}

pie_fig = go.Figure(data=go.Pie(
    labels=list(survey_data.keys()),
    values=list(survey_data.values()),
    # hole: 도넛 차트의 가운데 구멍 크기, 0~1 실수
    hole=0.3
))

pie_fig.update_layout(
    title='고객 만족도 설문 결과',
    height=400
)

st.subheader('만족도 분포')
st.plotly_chart(pie_fig, use_container_width=True)


# 4. 히스토그램으로 분포 보기
# 학생들의 키 분포
np.random.seed(42)
heights = np.random.normal(170, 10, 200)

hist_fig = go.Figure()
hist_fig.add_trace(go.Histogram(
    x=heights,
    nbinsx=20,
    name='키 분포',
    showlegend=True, # 범례 라벨 표시
    marker_color='lightgreen'
))

hist_fig.update_layout(
    title='학생 키 분포',
    xaxis_title='키 (cm)',
    yaxis_title='학생 수',
    height=400
)

st.subheader('키 분포 히스토그램')
st.plotly_chart(hist_fig, use_container_width=True)