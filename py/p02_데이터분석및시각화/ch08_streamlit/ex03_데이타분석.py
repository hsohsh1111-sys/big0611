import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go

data = {
    '이름' : ['홍길동', '심은하', '손예진', '김태희'],
    '수학' : [85, 92, 74, 65],
    '영어' : [75, 52, 84, 67],
    '과학' : [85, 92, 74, 65]
}

df = pd.DataFrame(data)

st.title('학생 성적 데이타 표시하기')
st.dataframe(df)

sales_data = {
    '상품명': ['노트북', '마우스', '키보드', '모니터', '헤드셋'],
    '가격': [1200000, 25000, 80000, 350000, 150000],
    '판매량': [15, 120, 85, 30, 45],
    '평점': [4.5, 4.2, 4.7, 4.1, 4.6]
}
df = pd.DataFrame(sales_data)

def color_rating(val):
    if val >= 4.5:
        color = 'green'
    elif val >=4.0:
        color = 'orange' 
    else:
        color = 'red'
    return f'color: {color}'

styled_df = df.style.format({
    '가격' : '{:,}원',
    '판매량' : '{:,}개',
    '평점' : '{:.1f}점'
    }).map(color_rating, subset=['평점'])

st.dataframe(styled_df)

weather_data = {
    '항목': ['최고 기온', '최저 기온', '습도', '강수 확률'],
    '값': ['28°C', '18°C', '65%', '30%']
}

weather_df = pd.DataFrame(weather_data)
st.table(weather_df)

dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
visitors = np.random.randint(100, 500, 30)

visitor_df = pd.DataFrame({
    'Date': dates,
    'Visitors': visitors
}) 

st.title('기본 차트 예시')
st.subheader('웹 사이트 일일 방문자 수')

st.line_chart(data=visitor_df, x='Date', y='Visitors')

population_data = {
    '서울': 9720000,
    '부산': 3390000,
    '인천': 2950000,
    '대구': 2410000,
    '대전': 1490000
}

population_df = pd.DataFrame(list(population_data.items()), columns=['도시', '인구수'])

st.subheader('주요 도시 인구 비교')
st.bar_chart(population_df.set_index('도시')['인구수'])

monthly_data = pd.DataFrame({
    'Date': dates,
    '온라인_매출': np.random.randint(50, 150, 30),
    '오프라인_매출': np.random.randint(80, 200, 30),
    '모바일_매출': np.random.randint(30, 100, 30)
})

st.subheader('채널별 매출 구성 변화')
st.area_chart(monthly_data.set_index('Date'))

dates = [datetime.now() - timedelta(days=x) for x in range(100, 0, -1)]
np.random.seed(42)
sales = np.random.randint(50, 200, 100)

# Plotly 선 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=dates,
    y=sales,
    mode='lines',
    name='일일 판매량',
    line=dict(color='blue', width=2)
))

fig.update_layout(
    title='인터랙티브 판매량 차트',
    xaxis_title='날짜',
    yaxis_title='판매량 (개)',
    height=400
)

st.plotly_chart(fig, use_container_width=True)


# 광고비와 매출의 관계
np.random.seed(42)
ad_spend = np.random.randint(10, 100, 50)
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
    hole=0.3
))

pie_fig.update_layout(
    title='고객 만족도 설문 결과',
    height=400
)

st.subheader('만족도 분포')
st.plotly_chart(pie_fig, use_container_width=True)

