from forecast.rain import minutes_to_rain
import logging
from sys import stdout
from common import scheduler
from common import sendmail
from tests import test_state


state = test_state.RainNotificationStateMachine()


def loop():
    minutes = minutes_to_rain()
    logging.info('Pluie dans ' + str(minutes) + ' minutes')
    if state.notify_rain(minutes):
        logging.warning('Notification: Pluie dans ' + str(minutes) + ' minutes')
        sendmail.send_mail('Pluie dans ' + str(minutes) + ' minutes', "A l'abri !!!")


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)s %(filename)s:%(lineno)d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO,
                        stream=stdout)
    # logging.info('Minutes avant la pluie : ' + str(minutes_to_rain()))

    sched = scheduler.Scheduler(delay=60*5, callback=loop)
    sched.start()
