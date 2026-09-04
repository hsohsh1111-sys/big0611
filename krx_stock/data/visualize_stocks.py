import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import os


# CSV 파일 로드 (절대 경로 사용)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "korean_stocks_2025_2026.csv")
df = pd.read_csv(csv_path)

# 날짜 형식 변환
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 종목명 매핑
stock_names = {
    "005930": "삼성전자",
    "035720": "카카오", 
    "005380": "현대차"
}

# ============================================================
# 1. 종목별 종가 차트 (라인 차트)
# ============================================================

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

fig1.write_html("stock_price_chart.html")
print("종가 차트 저장 완료: stock_price_chart.html")

# ============================================================
# 2. 종목별 거래량 차트
# ============================================================

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

fig2.write_html("stock_volume_chart.html")
print("거래량 차트 저장 완료: stock_volume_chart.html")

# ============================================================
# 3. 개별 종목 상세 차트 (종가 + 거래량)
# ============================================================

for code, name in stock_names.items():
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
    
    filename = f"stock_detail_{code}.html"
    fig.write_html(filename)
    print(f"{name} 상세 차트 저장 완료: {filename}")

# ============================================================
# 4. 수익률 비교 차트
# ============================================================

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

fig4.write_html("stock_return_rate.html")
print("수익률 차트 저장 완료: stock_return_rate.html")

print("\n모든 차트 생성 완료!")
