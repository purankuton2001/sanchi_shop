# import startVideoChat
# startVideoChat.start_video_chat()


from communications import comm


def eventKick(arg):
    print('kick' + str(arg))


if __name__ == '__main__':
    # イベントキック検証
    comm = comm.Comm('/dev/cu.usbmodem1411', 9)
    comm += eventKick
