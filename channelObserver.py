import serial
import startVideoChat
import time
import clickImage

def channel_observer(window):
    ser = serial.Serial('COM7', 9600, timeout=None)
    pre_val = 1

    # 画像ファイルのパス
    close_img_path = "image/closeButton.png"
    finish_img_path = "image/finishButton.png"

    while True:
        val_arduino = ser.readline()
        val_decoded = int(repr(val_arduino.decode())[1:-5])
        if val_decoded != pre_val and pre_val == 3:
            clickImage.click_image(close_img_path)
            time.sleep(0.5)
            clickImage.click_image(finish_img_path)
            time.sleep(3.0)
        if val_decoded == 1:
            window.load_url('https://www.youtube.com/embed/xxCzQ4ampo4?rel=0')
            pre_val=1
        elif val_decoded == 2:
            window.load_url('https://www.google.com/')
            pre_val=2
        else:
            startVideoChat.start_video_chat(window)
            pre_val=3

    ser.close()
