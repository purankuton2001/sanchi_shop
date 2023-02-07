import platform

import serial
import startVideoChat
import time
import pyautogui
import json
import adminScreen
import tkinter as tk
from tkinter import ttk




def channel_observer(window):
    pre_val = 1
    with open('setting.json', 'r') as f:
        api = json.load(f)

    if api['test_mode'] == True:
        root = tk.Tk()
        root.title("Channel Control")
        root.geometry("300x200")
        root.attributes("-topmost", True)
        frame = ttk.Frame(root)
        frame.pack()

        current_chan_label = ttk.Label(frame, text="Current Channel: 1")
        current_chan_label.pack()

        def change_channel(channel):
            nonlocal api, window, current_chan_label, pre_val
            if pre_val == 3:
                device = platform.system()
                if device == 'Windows':
                    pyautogui.hotkey('alt', 'q')
                elif device == 'macOS':
                    pyautogui.hotkey('command', 'q')
                time.sleep(0.5)
                pyautogui.hotkey('enter')
                time.sleep(3.0)
            pre_val = channel

            for index, value in enumerate(api["channel_setting"]):
                if channel == index + 1:
                    if value == 'zoom':
                        startVideoChat.start_video_chat(window)
                    else:
                        window.load_url(value)
                    current_chan_label.config(text="Current Channel: " + str(channel))

        def on_key_release(event):
            if event.char != '':
                change_channel(int(event.char))

        channel_1_btn = ttk.Button(frame, text="Channel 1", command=lambda: change_channel(1))
        channel_1_btn.pack()
        channel_2_btn = ttk.Button(frame, text="Channel 2", command=lambda: change_channel(2))
        channel_2_btn.pack()
        channel_3_btn = ttk.Button(frame, text="Channel 3", command=lambda: change_channel(3))
        channel_3_btn.pack()

        def quit_app():
            nonlocal root, window
            window.destroy()
            root.destroy()
        quit_btn = ttk.Button(frame, text="Quit", command=quit_app)
        quit_btn.pack()

        root.bind('<KeyRelease>', on_key_release)
        root.mainloop()
    else:
        try:
            ser = serial.Serial(api['serial_port'], 9600, timeout=None)
            while True:
                val_arduino = ser.readline()
                print(str(val_arduino))
                current_chan = int(repr(val_arduino.decode())[1:-5])
                if pre_val == 3:
                    device = platform.system()
                    if device == 'Windows':
                        pyautogui.hotkey('alt', 'q')
                    elif device == 'macOS':
                        pyautogui.hotkey('command', 'q')
                    time.sleep(0.5)
                    pyautogui.hotkey('enter')
                    time.sleep(3.0)
                for index, value in enumerate(api["channel_setting"]):
                    if current_chan == index+1:
                        if value != 'zoom':
                            window.load_url(value)
                        else:
                            startVideoChat.start_video_chat(window)
                        pre_val = index+1

            ser.close()
        except Exception as e:
            print(str(e))
            window.destroy()
            adminScreen.admin_screen(True)

