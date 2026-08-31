import pandas as pd
import matplotlib.pyplot as plt

from ex06_데이터조회 import db_select

# 데이터 분석
# 추출 결과 데이터프레임으로 저장
colnames = ['seq', 'dt', 'item_name', 'item_code', 'price', 'foreign_ownership_ratio', 'rel_return', 'per', 'per_12m', 'per_ind', 'pbr', 'dividend_yield', 'volume', 'trans_price', 'market_capital_prefer', 'market_capital_common']

rows = db_select()

df = pd.DataFrame(rows, columns=colnames)
print(df)

df_sam = df[df['item_name']=='삼성전자']
df_sk = df[df['item_name']=='SK하이닉스']

print(df_sam)
print(df_sk)


# 삼성전자 주식 데이터 시각화
plt.figure(figsize=(10, 10))

plt.subplot(5, 2, 1)
plt.plot(df_sam['dt'], df_sam['price'], color='blue', marker='o', linestyle='-')
plt.title('price')
plt.xticks(rotation=45)

plt.subplot(5, 2, 2)
plt.plot(df_sam['dt'], df_sam['foreign_ownership_ratio'], color='red', marker='o', linestyle='-')
plt.title('foreign_ownership_ratio')
plt.xticks(rotation=45)

plt.subplot(5, 2, 3)
plt.plot(df_sam['dt'], df_sam['rel_return'], color='brown', marker='o', linestyle='-')
plt.title('rel_return')
plt.xticks(rotation=45)

plt.subplot(5, 2, 4)
plt.plot(df_sam['dt'], df_sam['per'], color='orange', marker='o', linestyle='-')
plt.title('per')
plt.xticks(rotation=45)

plt.subplot(5, 2, 5)
plt.plot(df_sam['dt'], df_sam['pbr'], color='green', marker='o', linestyle='-')
plt.title('pbr')
plt.xticks(rotation=45)

plt.subplot(5, 2, 6)
plt.plot(df_sam['dt'], df_sam['dividend_yield'], color='purple', marker='o', linestyle='-')
plt.title('dividend_yield')
plt.xticks(rotation=45)

plt.subplot(5, 2, 7)
plt.plot(df_sam['dt'], df_sam['volume'], color='gray', marker='o', linestyle='-')
plt.title('volume')
plt.xticks(rotation=45)

plt.subplot(5, 2, 8)
plt.plot(df_sam['dt'], df_sam['trans_price'], color='pink', marker='o', linestyle='-')
plt.title('trans_price')
plt.xticks(rotation=45)

plt.subplot(5, 2, 9)
plt.plot(df_sam['dt'], df_sam['market_capital_prefer'], color='olive', marker='o', linestyle='-')
plt.title('market_capital_prefer')
plt.xticks(rotation=45)

plt.subplot(5, 2, 10)
plt.plot(df_sam['dt'], df_sam['market_capital_common'], color='cyan', marker='o', linestyle='-')
plt.title('market_capital_common')
plt.xticks(rotation=45)

plt.subplots_adjust(hspace=1.5)
plt.show()