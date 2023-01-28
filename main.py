from communications import comm
import startVideoChat
import channelObserver
import webview

window = webview.create_window(
    title='Screen',
    fullscreen=True
)
webview.start(startVideoChat.start_video_chat, window)

def eventKick(arg):
    print('kick' + str(arg))


if __name__ == '__main__':
    # イベントキック検証
    comm = comm.Comm('/dev/cu.usbmodem1411', 9)
    comm += eventKick
