import json

from linebot import LineBotApi
from linebot.models import TextSendMessage

from pyzoom import ZoomClient
import datetime

import time
import clickImage
import pyautogui
import adminScreen
import platform



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




def start_video_chat(window):
    with open('setting.json', 'r') as f:
        api = json.load(f)
    try:
        client = ZoomClient(api["api_setting"]["zoom_api_key"], api["api_setting"]["zoom_api_secret"])
        bot_api = LineBotApi(api["api_setting"]['line_access_token'])  # インスタンス化
        start_time = datetime.datetime.now() + datetime.timedelta(hours=-9)
        meeting = client.meetings.create_meeting('Auto created 1', start_time=start_time.isoformat(), duration_min=60,
                                                 password='not-secure')
        user_id = api["api_setting"]['line_userid']  # IDを取得
        messages = TextSendMessage(text=meeting.join_url)  # LINEに送付するメッセージ
        bot_api.multicast([user_id], messages=messages)
        window.load_url(meeting.join_url)
    except:
        print('channel')
        window.destroy()
        adminScreen.admin_screen(True)
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
    device = platform.system()
    if device == 'Windows':
        pyautogui.hotkey('alt','f')
    elif device == 'macOS':
        pyautogui.hotkey('command','shift','f')








