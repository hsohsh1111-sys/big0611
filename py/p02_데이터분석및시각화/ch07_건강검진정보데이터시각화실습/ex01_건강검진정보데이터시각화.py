import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams['font.family'] = 'NanumGothic'

df = pd.read_csv('국민건강보험공단_건강검진정보_2023.csv', encoding='euc-kr')

df.info()

df.drop(['기준년도', '치아마모증유무', '제3대구치(사랑니) 이상'], inplace=True, axis = 1)

df.rename(columns={'연령대코드(5세단위)':'연령코드', '신장(5cm단위)': '신장', '체중(5kg단위)': '체중', '식전혈당(공복혈당)': '혈당'}, inplace=True)

df.info()

fig, axs = plt.subplots(5, 5)
fig.set_size_inches(20, 24)

for i in range(0, 5):
    for j in range(5):
        attr = i * 5 + j + 1
        if df[df.columns[attr]].nunique() < 30:
            sns.countplot(data=df, x=df.columns[attr], ax=axs[i][j])
        else:
            sns.histplot(data=df, x=df.columns[attr],  kde=True, ax=axs[i][j])
df.columns
attr

df.columns[attr]
df['음주여부']

sns.scatterplot(x=df['수축기혈압'], y=df['이완기혈압'], hue=df['흡연상태'])

sns.scatterplot(x=df['신장'], y=df['체중'], hue=df['성별코드'])

sns.scatterplot(x=df['혈당'], y=df['총콜레스테롤'], hue=df['성별코드'])

sns.lineplot(x=df['연령코드'], y=df['총콜레스테롤'])

fig = plt.figure(figsize=(10,5))
sns.boxplot(x=df['연령코드'], y=df['혈색소'])

fig = plt.figure(figsize=(12,5))
sns.barplot(x=df['연령코드'], y=df['혈당'], hue=df['성별코드'])

fig = plt.figure(figsize=(10,5))
sns.boxplot(x=df['연령코드'], y=df['혈색소'])

fig = plt.figure(figsize=(12,5))
sns.barplot(x=df['연령코드'], y=df['혈당'], hue=df['성별코드'])

pivot_df = df.pivot_table('혈당', '시도코드', '연령코드')
sns.heatmap(pivot_df)