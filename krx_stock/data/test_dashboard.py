import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="테스트", layout="wide")

st.title("테스트 대시보드")

# 간단한 테스트 데이터
test_data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
}

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=test_data['x'],
    y=test_data['y'],
    mode='lines+markers',
    name='테스트 데이터'
))

fig.update_layout(
    title='테스트 그래프',
    xaxis_title='X',
    yaxis_title='Y'
)

st.plotly_chart(fig, width='stretch')

st.success("그래프가 보이면 성공!")
