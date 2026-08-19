import streamlit as st
from streamlit_autorefresh import st_autorefresh

# st_autorefresh(interval=1000, key="datarefresh")

st_autorefresh()

st.title('안녕하세요 streamlit')
st.write('이것은 나의 첫 번째 Streamlit 어플리케이션입니다.')
st.header('이것은 나의 st.header 어플리케이션입니다.')
st.subheader('이것은 나의 st.subheader 어플리케이션입니다.')
st.text('일반적인 텍스트')

st.markdown('**이것을 굵은 글씨입니다.**')
st.markdown('*이것은 기울어진 글씨*')
st.markdown('이것은 글씨')

st.write('안녕하세요!')
st.write(123)
st.write([1,2,3,4,5])

fruit = st.selectbox(
    '좋아하는 과일 선택',
    ['사과', '포도', '바나나']
)
st.write(f'당신이 선택한 과일은 {fruit}입니다.')

name = st.text_input('이름')
age = st.text_input('나이')

if name and age:
    st.write(f'{name}님은 {age}입니다')

temperature = st.slider('온도', 0, 40, 25)
st.write(f'선택한 온도는 {temperature}입니다.')

color = st.radio(
    '좋아하는 색깔',
    ['빨강', '노랑', '초록']
)

agree = st.checkbox('이용약관 동의')
if agree:
    st.write('동의해주셔서 감사합니다.')

hobbies = st.multiselect(
    '취미선택(여러개 가능)',
    ['독서', '여행', '영화감상', '운동', '음악감상']
)

if hobbies:
    st.write('선택한 취미:', hobbies)

today = st.date_input('날짜를 선택')
current_time = st.time_input('시간 선택')

st.write(f'선택한 날짜: {today}')
st.write(f'선택한 시간: {current_time}')

st.image('http://picsum.photos/200/300', caption='인터넷 이미지')
st.image('https://picsum.photos/id/237/200/300', caption='인터넷')
st.image('https://picsum.photos/seed/picsum/200/300', caption='인터넷', width=300)

st.image('my_image.jpg', caption='내 이미지', width=600)

st.video('my_video.mp4', width=300)

st.video('https://youtu.be/9-fmwaooLoI?si=_JXdci1hvUHkVGpy')

st.audio('my_audio.mp3')