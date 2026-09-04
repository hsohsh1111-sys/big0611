import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


# 페이지 설정
st.set_page_config(
    page_title="한국 주식 대시보드",
    page_icon="📈",
    layout="wide"
)

# ============================================================
# 데이터 로드 함수
# ============================================================

@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "korean_stocks_2025_2026.csv")
    
    # 디버깅용 경로 출력
    st.write(f"CSV 파일 경로: {csv_path}")
    st.write(f"파일 존재 여부: {os.path.exists(csv_path)}")
    
    if not os.path.exists(csv_path):
        st.error(f"CSV 파일을 찾을 수 없습니다: {csv_path}")
        return None
        
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    
    # 데이터 확인
    st.write(f"로드된 데이터 행 수: {len(df)}")
    st.write("데이터 미리보기:")
    st.dataframe(df.head())
    
    return df

@st.cache_data
def calculate_returns(df):
    df_copy = df.copy()
    df_copy['return_rate'] = df_copy.groupby('code')['close'].pct_change() * 100
    return df_copy

# ============================================================
# 그래프 생성 함수들
# ============================================================

def create_price_chart(df):
    fig = go.Figure()
    
    stock_names = {
        "005930": "삼성전자",
        "035720": "카카오", 
        "005380": "현대차"
    }
    
    for code, name in stock_names.items():
        stock_data = df[df['code'] == code].sort_values('date')
        fig.add_trace(go.Scatter(
            x=stock_data['date'],
            y=stock_data['close'],
            mode='lines',
            name=name,
            line=dict(width=2),
            hovertemplate=f'{name}<br>날짜: %{{x}}<br>종가: %{{y:,.0f}}원<extra></extra>'
        ))
    
    fig.update_layout(
        title='주식 종가 추이 (2025-2026)',
        xaxis_title='날짜',
        yaxis_title='종가 (원)',
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_volume_chart(df):
    fig = go.Figure()
    
    stock_names = {
        "005930": "삼성전자",
        "035720": "카카오", 
        "005380": "현대차"
    }
    
    for code, name in stock_names.items():
        stock_data = df[df['code'] == code].sort_values('date')
        fig.add_trace(go.Scatter(
            x=stock_data['date'],
            y=stock_data['volume'],
            mode='lines',
            name=name,
            line=dict(width=2),
            hovertemplate=f'{name}<br>날짜: %{{x}}<br>거래량: %{{y:,.0f}}<extra></extra>'
        ))
    
    fig.update_layout(
        title='주식 거래량 추이 (2025-2026)',
        xaxis_title='날짜',
        yaxis_title='거래량',
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

def create_detail_chart(df, code, name):
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
    
    return fig

def create_return_chart(df):
    fig = go.Figure()
    
    stock_names = {
        "005930": "삼성전자",
        "035720": "카카오", 
        "005380": "현대차"
    }
    
    for code, name in stock_names.items():
        stock_data = df[df['code'] == code].sort_values('date')
        fig.add_trace(go.Scatter(
            x=stock_data['date'],
            y=stock_data['return_rate'],
            mode='lines',
            name=name,
            line=dict(width=2),
            hovertemplate=f'{name}<br>날짜: %{{x}}<br>수익률: %{{y:.2f}}%<extra></extra>'
        ))
    
    fig.update_layout(
        title='일일 수익률 비교 (2025-2026)',
        xaxis_title='날짜',
        yaxis_title='수익률 (%)',
        hovermode='x unified',
        template='plotly_dark',
        height=500
    )
    
    return fig

# ============================================================
# 메인 앱
# ============================================================

def main():
    st.title("📈 한국 주식 대시보드")
    st.markdown("삼성전자, 카카오, 현대차 주가 데이터 분석 (2025-2026)")
    
    # 데이터 로드
    try:
        df = load_data()
        st.success("데이터 로드 완료!")
        st.info(f"총 {len(df)}건의 데이터가 로드되었습니다.")
    except Exception as e:
        st.error(f"데이터 로드 실패: {e}")
        return
    
    df_with_returns = calculate_returns(df)
    
    # 사이드바
    st.sidebar.header("설정")
    
    # 종목 선택
    stock_names = {
        "005930": "삼성전자",
        "035720": "카카오", 
        "005380": "현대차"
    }
    
    selected_stock = st.sidebar.selectbox(
        "종목 선택",
        options=list(stock_names.keys()),
        format_func=lambda x: stock_names[x]
    )
    
    # 탭 생성
    tab1, tab2, tab3, tab4 = st.tabs(["📊 전체 종가", "📉 전체 거래량", "🔍 종목 상세", "💰 수익률 비교"])
    
    with tab1:
        st.subheader("전체 종목 종가 추이")
        try:
            fig1 = create_price_chart(df)
            st.plotly_chart(fig1, width='stretch')
        except Exception as e:
            st.error(f"그래프 생성 실패: {e}")
        
        # 데이터 테이블
        st.subheader("최근 데이터")
        latest_data = df.sort_values('date').groupby('code').last().reset_index()
        latest_data['name'] = latest_data['code'].map(stock_names)
        display_cols = ['name', 'date', 'close', 'volume', 'change_rate']
        st.dataframe(latest_data[display_cols].rename(columns={
            'name': '종목명',
            'date': '날짜',
            'close': '종가',
            'volume': '거래량',
            'change_rate': '변동률(%)'
        }))
    
    with tab2:
        st.subheader("전체 종목 거래량 추이")
        try:
            fig2 = create_volume_chart(df)
            st.plotly_chart(fig2, width='stretch')
        except Exception as e:
            st.error(f"그래프 생성 실패: {e}")
    
    with tab3:
        st.subheader(f"{stock_names[selected_stock]} 상세 분석")
        try:
            fig3 = create_detail_chart(df, selected_stock, stock_names[selected_stock])
            st.plotly_chart(fig3, width='stretch')
        except Exception as e:
            st.error(f"그래프 생성 실패: {e}")
        
        # 해당 종목 데이터 테이블
        stock_data = df[df['code'] == selected_stock].sort_values('date', ascending=False).head(10)
        st.subheader("최근 10일 데이터")
        display_cols = ['date', 'open', 'high', 'low', 'close', 'volume']
        st.dataframe(stock_data[display_cols].rename(columns={
            'date': '날짜',
            'open': '시가',
            'high': '고가',
            'low': '저가',
            'close': '종가',
            'volume': '거래량'
        }))
    
    with tab4:
        st.subheader("일일 수익률 비교")
        try:
            fig4 = create_return_chart(df_with_returns)
            st.plotly_chart(fig4, width='stretch')
        except Exception as e:
            st.error(f"그래프 생성 실패: {e}")
        
        # 수익률 통계
        st.subheader("수익률 통계")
        stats = df_with_returns.groupby('code')['return_rate'].agg(['mean', 'std', 'min', 'max']).reset_index()
        stats['name'] = stats['code'].map(stock_names)
        stats.columns = ['종목코드', '종목명', '평균수익률', '표준편차', '최소수익률', '최대수익률']
        st.dataframe(stats)

if __name__ == "__main__":
    main()
