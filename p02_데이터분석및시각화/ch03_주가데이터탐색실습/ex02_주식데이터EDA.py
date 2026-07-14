import yfinance as yf
import pandas as pd

df = yf.download("NVDA", period="1y", interval="1d", multi_level_index = False)
df.head()
print("Shape:", df.shape)
print("\n=====Info:=====")
df.info()
print("\n=====Describe:=====")
print(df.describe())
print('컬럼명:', df.columns.tolist())
print('데이타타입:')
print(df.dtypes)
print("첫 5개 행:")
print(df.head(3))
print(f"종가 최대값: {df['Close'].max():,.0f}")
print(f"종가 최소값: {df['Close'].min():,.0f}")
print(f"종가 평균값: {df['Volume'].mean():,.0f}")
print(f"종가 중앙값: {df['Volume'].median():,.0f}")
print(f"종가 표준편차: {df['Volume'].std():,.0f}")
high_low_diff = df['High'] - df['Low']
print(f"고가와 저가의 차이 평균: {high_low_diff.mean():,.2f}")

selected_df = df[['Close', 'Volume']].copy()
selected_df.head()
recent_10 = df.tail(10)
recent_10
threshold = df['Close'].quantile(0.90)
high_price = df[df['Close'] >= threshold]
print(f"종가 {threshold:.2f} 이상인 날: {len(high_price)}일")

avg_volume = df['Volume'].mean()
high_volume_days = df[df['Volume'] > avg_volume]
print(f"평균 거래량({avg_volume:,.0f})보다 많았던 날: {len(high_volume_days)}일")
volume_sorted = df.sort_values('Volume', ascending=False)
print(volume_sorted['Volume'].head())

df['Daily_Change'] = df['Close'] - df['Open']
print(df[['Open', 'Close', 'Daily_Change']].head())


df['Change_Rate'] = ((df['Close'] - df['Open']) / df['Open'] * 100).round(2)
print(df[['Open', 'Close', 'Change_Rate']].head())

df['Year'] = df.index.year
df['Month'] = df.index.month
df['Weekday'] = df.index.day_name()
print(df[['Year', 'Month', 'Weekday']].head())

monthly_stats = df.groupby('Month').agg({
    'Close': 'mean',
    'Volume': 'sum'
}).round(0)
print(monthly_stats)

yearly_stats = df.groupby('Year').agg({
    'High': 'max',
    'Low': 'min'
})
print(yearly_stats)