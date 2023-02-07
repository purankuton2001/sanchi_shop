from tkinter import *
from tkinter import ttk
import json
import os
from tkinter import messagebox

import webview

import channelObserver

from tkinter import filedialog
import shutil


def select_file():
    file_path = filedialog \
        .askopenfilename(initialdir="/",
                         title="オーディオに参加",
                         filetypes=(("画像ファイル", "*.png;*.jpg"), ("すべてのファイル", "*.*")))
    return file_path


def replace_file(src, dst):
    if dst != '':
        shutil.copy(src, dst)


def on_click_start(api_setting_entries, channel_setting_entries, api, checkbutton,serial_port, root):
    save_json(api_setting_entries, channel_setting_entries, api, checkbutton,serial_port, root)
    window = webview.create_window(
        title='Screen',
        fullscreen=True
    )
    webview.start(channelObserver.channel_observer, window)


def save_json(api_setting_entries, channel_setting_entries, api, checkbutton, serial_port, root):
    for k, v in api_setting_entries.items():
        api["api_setting"][k] = v.get()

    for index, item in enumerate(channel_setting_entries):
        new_text = item.get()
        api["channel_setting"][index] = new_text if new_text else 'zoom'

    api["test_mode"] = checkbutton.get()
    api["serial_port"] = serial_port.get()
    root.destroy()
    with open('setting.json', 'w') as f:
        json.dump(api, f, indent=4)


def admin_screen(error=None):
    with open('setting.json', 'r') as f:
        api = json.load(f)

    root = Tk()
    root.title("sanchi_shop")

    api_setting_entries = {}
    for k, v in api["api_setting"].items():
        api_setting_entries[k] = ttk.Entry(root, textvariable=StringVar(), width=30)
        api_setting_entries[k].insert(0, v)

    label_line_title = ttk.Label(root, text='Line')
    label_serial_title = ttk.Label(root, text='シリアルポート')
    label_line_userid = ttk.Label(root, text='ユーザーID')
    label_line_access_token = ttk.Label(root, text='アクセストークン')

    label_zoom_title = ttk.Label(root, text='Zoom')
    click_image_title = ttk.Label(root, text='クリックする画像')
    label_zoom_userid = ttk.Label(root, text='Apiキー')
    label_zoom_access_token = ttk.Label(root, text='Apiシークレット')

    checkbutton_test_mode_var = BooleanVar(value=api['test_mode'])
    checkbutton_test_mode = ttk.Checkbutton(root, text='テストモード', variable=checkbutton_test_mode_var)

    entry_serial = ttk.Entry(root, textvariable=StringVar())
    entry_serial.insert(0, api['serial_port'])

    channel_setting_entries = []
    combo_boxes = []
    channel_mode = ["url", "zoom"]
    label_channel_title = ttk.Label(root, text='チャンネル設定')
    replace_file_button = ttk.Button(root, text="オーディオに参加",
                                     command=lambda: replace_file(select_file(), "./image/connectAudioButton.png"))
    replace_file_button2 = ttk.Button(root, text="開く",
                                     command=lambda: replace_file(select_file(), "./image/openButton.png"))

    for index, item in enumerate(api["channel_setting"]):
        combo_boxes.append(ttk.Combobox(root, values=channel_mode))
        if item == "zoom":
            channel_setting_entries.append(ttk.Entry(root, textvariable=StringVar(), state=DISABLED, width=30))
            combo_boxes[index].set("zoom")
        else:
            channel_setting_entries.append(ttk.Entry(root, textvariable=StringVar(), state=NORMAL, width=30))
            channel_setting_entries[index].insert(0, item)
            combo_boxes[index].set("url")

        label_channel = ttk.Label(root, text=index + 1)

        label_channel_title.grid(row=6, column=0)

        label_channel.grid(row=7 + index, column=0)
        combo_boxes[index].grid(row=7 + index, column=1)
        channel_setting_entries[index].grid(row=7 + index, column=2)


    def callback(e):
        for index, item in enumerate(combo_boxes):
            mode = item.get()
            if mode == "zoom":
                channel_setting_entries[index].delete(0, END)
                channel_setting_entries[index]["state"] = DISABLED
            elif mode == "url":
                channel_setting_entries[index]["state"] = NORMAL

    for index, item in enumerate(combo_boxes):
        item.bind("<<ComboboxSelected>>", func=callback)

    button_start = ttk.Button(root, text='スタート',
                              command=lambda: on_click_start(api_setting_entries, channel_setting_entries, api,
                                                             checkbutton_test_mode_var,entry_serial, root))

    # レイアウト

    label_line_title.grid(row=0, column=0)
    label_line_userid.grid(row=1, column=0)
    label_line_access_token.grid(row=2, column=0)
    api_setting_entries["line_userid"].grid(row=1, column=1)
    api_setting_entries["line_access_token"].grid(row=2, column=1)


    label_zoom_title.grid(row=3, column=0)
    click_image_title.grid(row=4, column=2)
    label_zoom_userid.grid(row=4, column=0)
    api_setting_entries["zoom_api_key"].grid(row=4, column=1)
    label_zoom_access_token.grid(row=5, column=0)
    api_setting_entries["zoom_api_secret"].grid(row=5, column=1)
    replace_file_button.grid(row=5, column=2)
    replace_file_button2.grid(row=5, column=3)

    label_serial_title.grid(row=19, column=0)
    entry_serial.grid(row=19, column=1)
    checkbutton_test_mode.grid(row=20, column=2)
    button_start.grid(row=21, column=2)
    if error:
        messagebox.showinfo('エラー', 'エラーが発生したので停止しました。')
    root.mainloop()
