import time

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title='학생 성적 관리',
    page_icon='🏚', # win+.
    layout='wide'
)

# 콘테츠 삽입
st.title('페이지 설정이 완료된 애플리케이션')
st.write('이제 더 넓은 화면에서 볼 수 있습니다.!')

# 레이아웃 컴포넌트
# 1. 열로 나누어 배치하기
st.title('학생 정보 관리 시스템') # 1rem = 16px

# 4개의 열로 나누기
col1, col2, col3, col4 = st.columns(4)
# [DeltaGenerator(), DeltaGenerator(), DeltaGenerator(), DeltaGenerator()]
# print(st.columns(4))

with col1:
    # 2.25rem = 36px, 0.875rem = 14px
    st.metric('전체 학생 수', '245명') 
with col2:
    st.metric('평균 점수', '82.5명')
with col3:
    st.metric('출석률', '94.2%')
with col4:
    st.metric('과제 제출률', '87.8%')

# 2. 열의 크기 조정하기
# 첫 번째 열을 다른 열보다 2배 크게 만들기
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.write('메인 콘텐츠 영역 - 이 열이 가장 넓습니다.')
with col2:
    st.write('통계 정보')
with col3:
    st.write('빠른 메뉴')

# 3. 컨테이너로 묶기
with st.container():
    st.subheader('이번 달 도서관 현형')
    st.write('이 영역에는 도서관의 주요 통계가 표시됩니다.')
    st.metric('대출 도서 수', '1,245권')
    st.metric('신규 회원', '+23명')

# 4. 확장 가능한 섹션 -> 아코디언
with st.expander('상세 통계 정보'):
    st.write('여기에는 자세한 분석 결과가 들어갑니다.')
    st.write('평소에는 숨겨져 있다가 필요할 때만 펼쳐볼 수 있습니다.')


## 정보 표시 컴포넌트
# 1. 지표 카드 만들기
st.title('카페 매출 대시보드')

# 기본 지표
st.metric('오늘 매출', '450,000원')

# 변화량과 함께 표시
st.metric(
    label='일일 방문객',
    value='127명',
    delta='+23명' # 양수면 초록색
)

# 음수 변화량 (빨간색으로 표시됨)
st.metric(
    label='재고 수량', # 지표의 이름
    value='85개', # 현재값
    delta='-15개' # 변화량, 음수면 빨간색
)

# 2. 상태 메시지 표시하기
# 정보 메시지 (파란색)
st.info('시스템 점검이 예정되어 있습니다.')

# 성공 메시지 (초록색)
st.success('데이터 백업이 완료되었습니다!')

# 경고 메시지 (노란색)
st.warning('일부 기능이 제한될 수 있습니다.')

# 오류 메시지 (빨간색)
st.error('서버 연결에 실패했습니다.')

# 3. 로딩 표시하기
with st.spinner('학생 데이터를 처리하는 중 ...'):
    # 실제로는 데이터를 불러오는 코드가 들어감
    time.sleep(3) # 3초 대기 (예시)

st.success('처리 완료!')

# 4. 빈 공간 관리하기
# 빈 공간 만들기
placeholder = st.empty()

# 나중에 내용 채우기
time.sleep(2)
placeholder.text('검색 결과가 나타났습니다.')

# 내용 교체하기
time.sleep(2)
placeholder.success('검색이 완료되었습니다.')