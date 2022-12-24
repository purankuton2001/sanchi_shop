import serial
import startVideoChat

def channel_observer(window):

    ser = serial.Serial('COM3', 9600, timeout=None)
    while True:
        val_arduino = ser.readline()
        val_decoded = int(repr(val_arduino.decode())[1:-5])
        print(val_decoded)
        if val_decoded == 1:
            window.load_url('https://www.youtube.com/')
        elif val_decoded == 2:
            window.load_url('https://www.google.com/')
        else:
            startVideoChat.start_video_chat(window)

    ser.close()
