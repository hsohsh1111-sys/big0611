import pandas as pd

# 1. 혈액형 카테고리 정의 (A, B, O, AB)
blood_types = pd.CategoricalDtype(categories=['A', 'B', 'O', 'AB'])

# 2. 샘플 데이터 생성 (AB형은 데이터에 아예 없음)
data = {
    '성별': ['남', '여', '남', '여'],
    '혈액형': pd.Series(['A', 'B', 'O', 'A'], dtype=blood_types),
    '점수': [85, 92, 78, 88]
}
df = pd.DataFrame(data)

# 3. pivot_table 실행 비교
# [Case A] observed=False (기본값) -> 데이터에 없는 'AB'형도 테이블에 나타남
pivot_f = df.pivot_table(index='성별', columns='혈액형', values='점수', aggfunc='count', observed=False)
pivot_f

# [Case B] observed=True -> 실제 관측된 'A', 'B', 'O'만 나타남
pivot_t = df.pivot_table(index='성별', columns='혈액형', values='점수', aggfunc='count', observed=True)
pivot_t