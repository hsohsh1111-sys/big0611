import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.head()
sns.scatterplot(x=df['total_bill'], y=df['tip'])
plt.show()
sns.scatterplot(x=df['total_bill'], y=df['tip'], hue=df['sex'])
plt.show()
sns.scatterplot(x=df['total_bill'], y=df['tip'], hue=df['sex'], size=df['size'])
plt.show()
sns.scatterplot(x=df['total_bill'], y=df['tip'], 
                hue=df['sex'],      # 색상으로 성별 구분
                size=df['size'],    # 크기로 인원수 표현
                style=df['time'],   # 모양으로 시간대 구분
                alpha=0.7)          # 투명도 조절
plt.show()
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 42]
sns.scatterplot(x=x, y=y)
plt.show()
sns.barplot(x=x, y=y)
plt.show()