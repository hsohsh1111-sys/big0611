import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 2000ms(1초)마다 페이지 자동 새로고침
st_autorefresh(interval=1000, key="datarefresh")
# st_autorefresh()

st.title('Streamlit!!')
st.write('첫 번째 Streamlilt 애플리케이션입니다.') # 1rem = 16px

# 1. 제목과 헤더 만들기
st.title('이것은 가장 큰 제목입니다.') # 2.75rem = 44px
st.header('이것은 큰 헤더입니다.') # 2.25rem = 36px
st.subheader('이것은 작은 헤더입니다.') # 1.75rem = 28px

# 2. 일반 텍스트 표시하기
st.text('이것은 일반적인 텍스트입니다.') # 1rem = 16px
st.text('여러 줄로 텍스트를 작성할 수도 있습니다.')

# 3. 마크다운으로 꾸미기
st.markdown('**이것은 굵은 글씨입니다.**')
st.markdown('*이것은 기울어진 글씨입니다.*')
st.markdown('이것은 `인라인 코드` 입니다.')

# 4. 만능 출력 함수
st.write('안녕하세요!')
st.write(123)
st.write([1, 2, 3, 4, 5])


# 입력 컴포넌트
# 1. 선택 상자 만들기
# 좋아하는 과일 선택
fruit = st.selectbox(
    '좋아하는 과일을 선택하세요',
    ['사과', '바나나', '오렌지', '포도']
)
st.write(f'당신이 선택한 과일은 {fruit}입니다.')

# 2. 텍스트 입력받기
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이를 입력하세요', min_value=0, max_value=120)

if name and age:
    st.write(f'{name}님은 {age}살입니다.')

# 3. 슬라이드로 값 조정하기 <input type="range">
temperature = st.slider('온도를 선택하세요', 0, 40, 25)
st.write(f'선택한 온도는 {temperature}도 입니다.')

# 4. 라디오 버튼과 체크박스 <input type="radio|checkbox">
color = st.radio(
    '좋아하는 색갈을 선택하세요',
    ['빨강', '파랑', '초록']
)

agree = st.checkbox('이용약관에 동의합니다.')
if agree:
    st.write('동의해주셔서 감사합니다.')

# 5. 여러 개 선택하기
hobbies = st.multiselect(
    '취미를 선택하세요 (여러 개 선택 가능)',
    ['독서', '영화감상', '운동', '여행', '음악감상']
)

if hobbies:
    st.write('선택한 취미:', hobbies)

# 6. 날짜와 시간 입력
today = st.date_input('날짜를 선택하세요')
current_time = st.time_input('시간을 선택하세요')

st.write(f'선택한 날짜: {today}')
st.write(f'선택한 시간: {current_time}')


# 미디어 컴포넌트
# 1. 이미지 표시하기 
# <img src="경로/파일명" width=300 alt="대체텍스트">
# 비트맵(jpg, gif, png)
# 벡터(svg) -> 로고
# 인터넷 이미지 표시
# st.image('https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ba819fd9-0cbb-401a-9136-9fe3fcb23111/Home_Page.png', caption='예시 이미지')
# https://picsum.photos -> 더미이미지(랜덤 사진)
# https://unsplash.com/ko -> 사진
# https://www.pngwing.com/ko -> 심볼, 아이콘
st.image('https://picsum.photos/id/1000/300/200', caption='인터넷 이미지')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3hOvJTBItOZKSe5CRE8qikcegiRJTUUGeJ-zgWYrCZg&s=10', caption='2026 부동산', width=300)

# 로컬 이미지 파일 표시 (파일이 있는 경우)
st.image('my_image.jpg', caption='내 이미지', width=300)
st.image('unsplash.jpg', caption='아파트 사진', width=300)
st.image('pngwing.png', caption='로고')


# 2. 비디오

# 아파트 전문 부동산 플랫폼에 어울리는 메인 페이지의 상단 첫 번째 섹션에 배경 동영상으로 삽입할 가로 1920px의  mp4 파일로 만들어줘 단, 텍스트 없는 깔끔한 30초 내외 영상으로 만들어줘
'''
영상 컨셉
해상도 : 1920 × 1080 (16:9)
길이 : 30초
형식 : MP4
FPS : 30fps
텍스트 : 없음
로고 : 없음
사람 : 최소화 또는 등장하지 않음
분위기 : 프리미엄 · 신뢰감 · 모던
색감 : 화이트 + 블루 + 따뜻한 골드톤
루프가 자연스럽게 이어지는 구성
'''
# AI 영상 생성 프롬프트
# Ultra cinematic luxury apartment real estate hero video. 30 seconds. 1920x1080. No text. No logos. No watermark. Premium Korean metropolitan apartment lifestyle. Smooth slow camera movement. Modern luxury apartment towers at sunrise with soft golden light reflecting on glass buildings. Drone aerial shot over a clean modern city skyline. Elegant residential complexes surrounded by green parks and walking paths. Beautiful apartment interiors with large windows, natural sunlight, wooden floors, marble kitchen, modern living room, panoramic city view. Close-up of architectural details, balconies, smart home features, premium lobby, landscaped gardens. Transition to evening skyline with warm apartment lights. Soft clouds moving naturally. Minimal people or none visible. Clean cinematic composition. Realistic lighting, high dynamic range, shallow depth of field, smooth dolly movements, professional commercial quality, Netflix documentary style, Apple advertisement aesthetics, luxury real estate promotional video. Seamless ending matching beginning for looping background video. No captions. No typography. No branding. No camera shake.

# https://www.pexels.com/ko-kr/search/videos/?q=%EB%B6%80%EB%8F%99%EC%82%B0%20%EC%95%84%ED%8C%8C%ED%8A%B8
# 비디오 파일 재생
# <video src="경로/파일명"></video>
# mp4, webm, ogv(ogg)
st.video('my_video.mp4', width=300)

# 유튜브 비디오 표시 <iframe src="경로/파일명"></iframe>
st.video('https://youtu.be/BU-DXvjGEqg?si=71Rc4xQ5OiCBVFvA', width=300)


# 오디오 파일 재생
# 유튜브 오디오 보관함: https://studio.youtube.com/channel/UCkCxjM7byQ3sQMBqmO7it6g/music
# 무료 소리 창고: https://pgtd.tistory.com/270
# mp3(노래), ogg(ogv), wav(미디음)
st.audio('ding.mp3')
st.audio('my_audio.mp3')