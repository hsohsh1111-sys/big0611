# 데이터 시각화 실습
# 건강검진정보 데이터 시각화
# 데이터 준비 및 전처리
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 글꼴 변경: 한글 지원
plt.rcParams['font.family'] = 'NanumGothic'

df = pd.read_csv('국민건강보험공단_건강검진정보_2023.csv', encoding='euc-kr')

print(df.head())
print(df.describe())
print(df.info())

# 1. 불필요한 컬럼 제거 및 컬럼명 변경
# 컬럼 삭제 
df.drop(
    ['기준년도', '가입자일련번호' '결손치 유무', '치아마모증유무', '제3대구치(사랑니) 이상'],
    inplace=True, # 원본 수정
    axis=1
)

# 컬럼명 변경
df.rename(
    columns={
        '연령대코드(5세단위)': '연령코드',
        '신장(5cm단위)': '신장',
        '체중(5kg단위)': '체중',
        '식전혈당(공복혈당)': '혈당'
    },
    inplace=True
)

# 결측치(NaN) 제거
df = df.dropna()

print(df.info())


# 전체 데이터 분포 시각화
fig, axs = plt.subplots(5, 5)
fig.set_size_inches(20, 24)

for i in range(0, 5):
    for j in range(5):
        attr = i * 5 + j + 1
        if df[df.columns[attr]].nunique() < 30:
            sns.countplot(data=df, x=df.columns[attr], ax=axs[i][j])
        else:
            sns.histplot(data=df, x=df.columns[attr], kde=True, ax=axs[i][j])

# df[df.columns[attr]].nunique()
# df['음주여부'].nunique()
df
df.columns
attr
df.columns[attr] # 음주여부
df['음주여부']
df['음주여부'].nunique()


# 특정 컬럼 세부 분석
df['음주여부'].value_counts()
df['연령코드'].value_counts()


# 상관관계 분석
# 1. 혈압 데이터 상관관계
sns.scatterplot(x=df['수축기혈압'], y=df['이완기혈압'], hue=df['흡연상태'])

# 2. 신장과 체중 상관관계
sns.scatterplot(x=df['신장'], y=df['체중'], hue=df['성별코드'])

# 3. 혈당과 총 콜레스테롤 상관관계
sns.scatterplot(x=df['혈당'], y=df['총콜레스테롤'], hue=df['성별코드'])


# 연령별 분석
# 1. 나이에 따른 총 콜레스테롤 추이
sns.lineplot(x=df['연령코드'], y=df['총콜레스테롤'])

# 2. 연련에 따른 혈색소 수치 분포
fig = plt.figure(figsize=(10, 5))
sns.boxplot(x=df['연령코드'], y=df['혈색소'])

df.describe()


# 성별 및 연령별 비교 분석
# 1. 연령과 성별에 다른 혈당 분석
fig = plt.figure(figsize=(12, 5))
sns.barplot(x=df['연령코드'], y=df['혈당'], hue=df['성별코드'])

# 2. 나이에 따른 허리둘레 분포
fig = plt.figure(figsize=(12, 5))
sns.violinplot(x=df['연령코드'], y=df['허리둘레'], hue=df['성별코드'])


# 지역별 분석
# 1. 지역과 연령에 따른 혈당 수치 히트맵
pivot_df = df.pivot_table('혈당', '시도코드', '연령코드')
sns.heatmap(pivot_df)
