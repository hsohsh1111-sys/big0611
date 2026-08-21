import os
import requests
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 토큰과 채널 가져오기
token = os.getenv("SLACK_BOT_TOKEN")
channel = os.getenv("SLACK_CHANNEL", "#general")

text = "Check your stock crawler."

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})