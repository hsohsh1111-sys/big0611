import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# streamlit 페이지 설정
st.set_page_config(
    page_title='주식 분석기',
    page_icon='📈',
    layout='wide'
)

# 미국 주요 종목 딕셔너리 (심볼: 회사명)
STOCKS = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corp.',
    'GOOGL': 'Alphabet Inc.',
    'TSLA': 'Tesla Inc.',
    'NVDA': 'NVIDIA Corp.'
}

# 주식 데이터 가져오기 함수
def get_stock_data(symbol, period='1y'):
    '''
    Parameters:
    symbol (str): 주식 심볼 (예: 'AAPL')
    period (str): 데이터 기간 (예: '1y' - 1년, '6mo' - 6개월, '3mo' - 3개월)

    Returns:
    tuple: (역사적 데이터, 기업 정보) 또는 (None, None)
    '''
    try:
        # yfinance Ticker 객체 생성
        ticker = yf.Ticker(symbol)

        # 역사적 데이터 가져오기
        hist_data = ticker.history(period=period)

        # 기업 정보 가져오기
        company_info = ticker.info

        # 데이터가 비어있지 않으면 반환
        if not hist_data.empty:
            return hist_data, company_info
        else:
            return None, None
        
    except Exception as e:
        st.error(f'데이터를 가져오는 중 오류 발생: {e}')
        return None, None

# 기업 정보 표시 함수
def display_company_info(company_info, current_price):
    '''
    기업 기본 정보를 표시하는 함수

    Parameters:
    company_info (dict): 기업 정보 딕셔너리
    current_price (float): 현재 주가
    '''

    # 4개의 열로 나누기
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric('현재가', f'${current_price:.2f}')
    
    with col2:
        # 시가총액 가져오기 (없으면 0)
        market_cap = company_info.get('marketCap', 0)
        st.metric('시가총액', f'${market_cap:,.0f}')

    with col3:
        # PER 가져오기 (없으면 0)
        pe_ratio = company_info.get('trailingPE', 0)
        st.metric('PER', f'{pe_ratio:.2f}' if pe_ratio else 'N/A')

    with col4:
        # 배당수익률 가져오기
        dividend_yield = company_info.get('dividendYield', 0)
        if dividend_yield:
            st.metric('배당수익률', f'{dividend_yield * 100:.2f}%')
        else:
            st.metric('배당수익률', 'N/A')
		
# 주가 차트 생성 함수
def create_price_chart(hist_data, symbol):
    '''
    주가 캔들스틱 차트를 생성하는 함수

    Parameters:
    hist_data (DataFrame): 주가 역사적 데이터
    symbol (str): 주식 심볼

    Returns:
    plotly.graph_objects.Figure: 차트 객체
    '''

    # 빈 Figure 객체 생성
    fig = go.Figure()

    # 캔들스틱 차트 추가
    fig.add_trace(go.Candlestick(
        x=hist_data.index,
        open=hist_data['Open'],
        high=hist_data['High'],
        low=hist_data['Low'],
        close=hist_data['Close'],
        name=symbol
    ))

    # 20일 이동평균선 추가 (데이터가 20일 이상일 때)
    if len(hist_data) >= 20:
        ma20 = hist_data['Close'].rolling(window=20).mean()
        fig.add_trace(go.Scatter(
            x=hist_data.index,
            y=ma20,
            mode='lines',
            name='MA20',
            line=dict(color='orange', width=1)
        ))

    # 차트 레이아웃 설정
    fig.update_layout(
        title=f'{symbol} 주가 차트',
        yaxis_title='가격 ($)',
        xaxis_title='날짜',
        height=500
    )
    return fig
		
# 거래량 차트 생성 함수
def create_volume_chart(hist_data, symbol):
    '''
    거래량 차트를 생성하는 함수

    Parameters:
    hist_data (DataFrame): 주식 역사적 데이터
    symbol (str): 주식 심볼

    Returns:
    plotly.graph_objects.Figure: 차트 객체
    '''
    fig = go.Figure()

    # 거래량 막대 차트 추가
    fig.add_trace(go.Bar(
        x=hist_data.index,
        y=hist_data['Volume'],
        name='거래량',
        marker_color='lightblue'
    ))

    # 차트 레이아웃 설정
    fig.update_layout(
        title=f'{symbol} 거래량 차트',
        yaxis_title='거래량',
        xaxis_title='날짜',
        height=300
    )
    return fig
		
# 기술적 지표 계산 함수
def calculate_technical_indicators(hist_data):
    '''
    기술적 지표를 계산하는 함수

    Parameters:
    hist_data (DataFrame): 주식 역사적 데이터

    Returns:
    dict: 계산된 지표들의 딕셔너리
    '''
    # 일일 수익률 계산 (전일 대비 변화율)
    returns = hist_data['Close'].pct_change().dropna()

    # 기간 수익률 계산 (전체 기간)
    total_return = ((hist_data['Close'].iloc[-1] / hist_data['Close'].iloc[0]) - 1) * 100

    # 일일 평균 수익률
    avg_daily_return = returns.mean() * 100

    # 연간 변동성 (일일 변동성 x 루트252)
    volatility = returns.std() * np.sqrt(252) * 100

    # 최대 손실폭 (MDD) 계산
    cummax = hist_data['Close'].cummax() # 누적 최대값
    drawdown = (cummax - hist_data['Close']) / cummax
    max_drawdown = drawdown.max() * 100

    # 샤프 비율 (위험 대비 수익률)
    sharpe_ratio = avg_daily_return / returns.std() * np.sqrt(252) if returns.std() > 0 else 0

    return {
        'total_return': total_return,
        'avg_daily_return': avg_daily_return,
        'volatility': volatility,
        'max_drawdown': max_drawdown,
        'sharpe_ratio': sharpe_ratio,
    }
		
# 메인 앱 실행 함수
def main():
    # 앱 제목
    st.title('주식 분석 대시보드')

    # 종목 선택
    selected_symbol = st.selectbox(
        '분석할 종목을 선택하세요:',
        list(STOCKS.keys()),
        format_func=lambda x: f'{x} - {STOCKS[x]}'
    )

    # 기간 선택
    period_options = {
        '3개월': '3mo',
        '6개월': '6mo',
        '1년': '1y',
        '2년': '2y'
    }

    selected_period = st.selectbox('분석 기간:', list(period_options.keys()))
    period_code = period_options[selected_period]

    # 데이터 로딩
    with st.spinner('데이터를 가져오는 중...'):
        hist_data, company_info = get_stock_data(selected_symbol, period_code)

    # 데이터가 없으면 종료
    if hist_data is None:
        st.error('데이터를 가져올 수 없습니다.')
        return

    # 현재가 계산
    current_price = hist_data['Close'].iloc[-1]

    # 1. 기업 정보 표시
    display_company_info(company_info, current_price)

    # 2.주가 차트 표시
    st.subheader('주가 차트')
    price_chart = create_price_chart(hist_data, selected_symbol)
    st.plotly_chart(price_chart, use_container_width=True)

    # 3. 거래량 차트 표시
    st.subheader('거래량')
    volume_chart = create_volume_chart(hist_data, selected_symbol)
    st.plotly_chart(volume_chart, use_container_width=True)

    # 4. 기술적 지표 표시
    st.subheader('기술적 지표')
    indicators = calculate_technical_indicators(hist_data)

    # 지표를 데이터프레임으로 만들어 표시
    metrics_df = pd.DataFrame({
        '지표': ['총 수익률', '일일 평균 수익률', '연간 변동성', '최대 손실폭', '샤프 비율'],
        '값': [
            f'{indicators["total_return"]:.2f}%',
            f'{indicators["avg_daily_return"]:.3f}%',
            f'{indicators["volatility"]:.2f}%',
            f'{indicators["max_drawdown"]:.2f}%',
            f'{indicators["sharpe_ratio"]:.2f}'
        ]
    })

    st.dataframe(metrics_df, use_container_width=True)


# 앱 실행
if __name__ == '__main__':
    main()