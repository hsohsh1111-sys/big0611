import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


# 페이지 설정
st.set_page_config(
    page_title="한국 주식 시각화",
    page_icon="📈",
    layout="wide"
)

# CSV 파일 로드
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "korean_stocks_2025_2026.csv")

st.write(f"CSV 파일 경로: {csv_path}")
st.write(f"파일 존재 여부: {os.path.exists(csv_path)}")

if not os.path.exists(csv_path):
    st.error("CSV 파일을 찾을 수 없습니다!")
    st.stop()

df = pd.read_csv(csv_path)
st.write(f"데이터 로드 완료: {len(df)}행")

# 날짜 형식 변환
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 종목명 매핑
stock_names = {
    "005930": "삼성전자",
    "035720": "카카오", 
    "005380": "현대차"
}

st.title("📈 한국 주식 시각화 대시보드")
st.markdown("삼성전자, 카카오, 현대차 주가 데이터 분석 (2025-2026)")

st.write("데이터 미리보기:")
st.dataframe(df.head())

# ============================================================
# 1. 종목별 종가 차트 (라인 차트)
# ============================================================

st.header("1. 종목별 종가 추이")

fig1 = go.Figure()

for code, name in stock_names.items():
    stock_data = df[df['code'] == code].sort_values('date')
    fig1.add_trace(go.Scatter(
        x=stock_data['date'],
        y=stock_data['close'],
        mode='lines',
        name=name,
        line=dict(width=2),
        hovertemplate=f'{name}<br>날짜: %{{x}}<br>종가: %{{y:,.0f}}원<extra></extra>'
    ))

fig1.update_layout(
    title='주식 종가 추이 (2025-2026)',
    xaxis_title='날짜',
    yaxis_title='종가 (원)',
    hovermode='x unified',
    template='plotly_dark',
    height=500
)

st.plotly_chart(fig1, width='stretch')

# ============================================================
# 2. 종목별 거래량 차트
# ============================================================

st.header("2. 종목별 거래량 추이")

fig2 = go.Figure()

for code, name in stock_names.items():
    stock_data = df[df['code'] == code].sort_values('date')
    fig2.add_trace(go.Scatter(
        x=stock_data['date'],
        y=stock_data['volume'],
        mode='lines',
        name=name,
        line=dict(width=2),
        hovertemplate=f'{name}<br>날짜: %{{x}}<br>거래량: %{{y:,.0f}}<extra></extra>'
    ))

fig2.update_layout(
    title='주식 거래량 추이 (2025-2026)',
    xaxis_title='날짜',
    yaxis_title='거래량',
    hovermode='x unified',
    template='plotly_dark',
    height=500
)

st.plotly_chart(fig2, width='stretch')

# ============================================================
# 3. 개별 종목 상세 차트 (종가 + 거래량)
# ============================================================

st.header("3. 개별 종목 상세 분석")

selected_stock = st.selectbox(
    "종목 선택",
    options=list(stock_names.keys()),
    format_func=lambda x: stock_names[x]
)

code = selected_stock
name = stock_names[code]

stock_data = df[df['code'] == code].sort_values('date')

fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    row_heights=[0.7, 0.3],
    subplot_titles=(f'{name} 종가', f'{name} 거래량')
)

# 종가 차트
fig.add_trace(
    go.Scatter(
        x=stock_data['date'],
        y=stock_data['close'],
        mode='lines',
        name='종가',
        line=dict(color='#00ff00', width=2)
    ),
    row=1, col=1
)

# 거래량 차트
colors = ['red' if row['close'] < row['open'] else 'green' 
          for _, row in stock_data.iterrows()]

fig.add_trace(
    go.Bar(
        x=stock_data['date'],
        y=stock_data['volume'],
        name='거래량',
        marker_color=colors,
        opacity=0.7
    ),
    row=2, col=1
)

fig.update_layout(
    title=f'{name} 주가 상세 분석',
    template='plotly_dark',
    height=600,
    showlegend=False
)

fig.update_yaxes(title_text="종가 (원)", row=1, col=1)
fig.update_yaxes(title_text="거래량", row=2, col=1)

st.plotly_chart(fig, width='stretch')

# ============================================================
# 4. 수익률 비교 차트
# ============================================================

st.header("4. 일일 수익률 비교")

# 기준일(첫날) 대비 수익률 계산
df['return_rate'] = df.groupby('code')['close'].pct_change() * 100

fig4 = go.Figure()

for code, name in stock_names.items():
    stock_data = df[df['code'] == code].sort_values('date')
    fig4.add_trace(go.Scatter(
        x=stock_data['date'],
        y=stock_data['return_rate'],
        mode='lines',
        name=name,
        line=dict(width=2),
        hovertemplate=f'{name}<br>날짜: %{{x}}<br>수익률: %{{y:.2f}}%<extra></extra>'
    ))

fig4.update_layout(
    title='일일 수익률 비교 (2025-2026)',
    xaxis_title='날짜',
    yaxis_title='수익률 (%)',
    hovermode='x unified',
    template='plotly_dark',
    height=500
)

st.plotly_chart(fig4, width='stretch')

st.success("모든 차트 생성 완료!")
