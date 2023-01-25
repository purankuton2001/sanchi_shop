import pyfirmata
import time
import threading


class Comm:

    def __init__(self, port, pin):
        self.cnt = 0
        self.handler = []
        # self.board = pyfirmata.Arduino(port)

        while True:
            # TODO debug
            time.sleep(1)
            self.cnt += 1
            self.emit(self.cnt)

            # v = self.board.analog[pin].read()
            # if v == None:
            #     pass
            # else:
            #     self.emit(v)

    def add(self, handler):
        self.handler.append(handler)
        return self

    def remove(self, handler):
        self.handler.remove(handler)
        return self

    def emit(self, sender, arg=None):
        for handle in self.handler:
            handle(sender, arg)

    __iadd__ = add
    __isub__ = remove
    __call__ = emit
