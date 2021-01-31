import time


class Scheduler:
    def __init__(self, delay, callback):
        self.delay = delay
        self.callback = callback

    def start(self):
        while True:
            self.callback()
            time.sleep(self.delay)

    def update(self, delay):
        self.delay = delay


def _print():
    print("Event triggered")


if __name__ == '__main__':
    s = Scheduler(3, _print)
    s.start()
