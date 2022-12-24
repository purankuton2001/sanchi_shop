import startVideoChat
import channelObserver
import webview

window = webview.create_window(
    title='Screen',
    fullscreen=True
)
webview.start(channelObserver.channel_observer, window)






