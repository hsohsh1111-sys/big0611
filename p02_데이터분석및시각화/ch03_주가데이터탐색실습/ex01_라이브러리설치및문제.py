import yfinance as yf
import pandas as pd

df = yf.download("NVDA", period="1y", interval="1d", multi_level_index = False)
df.head()
print("Shape:", df.shape)
print("\n=====Info:=====")
df.info()
print("\n=====Describe:=====")
print(df.describe())