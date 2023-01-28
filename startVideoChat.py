import json

from linebot import LineBotApi
from linebot.models import TextSendMessage

from pyzoom import ZoomClient
import datetime

import googleapiclient.discovery
import google.auth
import time
import clickImage


with open('secret.json', 'r') as f:
    api = json.load(f)

SCOPES = ['https://www.googleapis.com/auth/calendar']
calendar_id = 'purankutonacount@gmail.com'
# Googleの認証情報をファイルから読み込む
credentials = google.auth.load_credentials_from_file('antenashop-0086fb76190a.json', SCOPES)[0]

gapi_creds = credentials.with_subject(calendar_id)
# APIと対話するためのResourceオブジェクトを構築する
service = googleapiclient.discovery.build('calendar', 'v3', credentials=gapi_creds)

body = {
    'conferenceData': {
        'createRequest': {
            'conferenceSolutionKey': {
                'type': 'hangoutsMeet'
            },
            'requestId': "123"
        },
    },
    # 予定のタイトル
    'summary': 'ミーティング③',
    # 予定の開始時刻
    'start': {
        'dateTime': datetime.datetime(2023, 2, 6, 10, 30).isoformat(),
        'timeZone': 'Japan'
    },
    # 予定の終了時刻
    'end': {
        'dateTime': datetime.datetime(2023, 2, 6, 12, 00).isoformat(),
        'timeZone': 'Japan'
    },
}
# 用意した予定を登録する


client = ZoomClient(api["zoom_api_key"], api["zoom_api_secret"])

bot_api = LineBotApi(api['line_access_token'])  # インスタンス化

def start_video_chat(window):
    start_time = datetime.datetime.now() + datetime.timedelta(hours=-9)
    # event = service.events().insert(calendarId=calendar_id, body=body, conferenceDataVersion=1).execute()
    meeting = client.meetings.create_meeting('Auto created 1', start_time=start_time.isoformat(), duration_min=60,
                                             password='not-secure')
    user_id = api['line_userid']  # IDを取得
    messages = TextSendMessage(text=meeting.join_url)  # LINEに送付するメッセージ
    bot_api.multicast([user_id], messages=messages)
    window.load_url(meeting.join_url)
    # 画像ファイルのパス
    open_img_path = "image/openButton.png"
    connect_audio_img_path = "image/connectAudioButton.png"
    maximize_img_path = "image/maximizeButton.png"

    # zoomアプリ起動
    time.sleep(1.0)
    clickImage.click_image(open_img_path)
    time.sleep(3.0)
    clickImage.click_image(connect_audio_img_path)
    time.sleep(1.0)
    clickImage.click_image(maximize_img_path)








