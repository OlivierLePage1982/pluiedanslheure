from forecast.rain import minutes_to_rain
import logging
from sys import stdout
from common import scheduler
from tests import test_state
from random import seed
from random import randint

state = test_state.RainNotificationStateMachine()


def detect_rain():
    array = [-1, 0, 15, 45]
    sentence = ['No rain', 'Rain in progress', 'Rain in 15 mins', 'Rain in 45 mins']
    index = randint(0, 3)
    print(sentence[index])
    return array[index]


def loop():
    minutes = detect_rain()
    if state.notify_rain(minutes):
        print('==> Notification !!!')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)s %(filename)s:%(lineno)d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO,
                        stream=stdout)
    logging.info('Minutes avant la pluie : ' + str(minutes_to_rain()))

    seed(1)
    sched = scheduler.Scheduler(delay=5, callback=loop)
    sched.start()
