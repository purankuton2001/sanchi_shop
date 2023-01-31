from communications import comm
import startVideoChat
import channelObserver
import webview
import adminScreen


adminScreen.admin_screen()


def eventKick(arg):
    print('kick' + str(arg))


if __name__ == '__main__':
    # イベントキック検証
    comm = comm.Comm('/dev/cu.usbmodem1411', 9)
    comm += eventKick
