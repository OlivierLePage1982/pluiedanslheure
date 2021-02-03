from forecast.rain import minutes_to_rain
import logging
from sys import stdout
from common import scheduler
from common import sendmail
from tests import test_state


state = test_state.RainNotificationStateMachine()


def loop():
    minutes = minutes_to_rain()
    if minutes >= 0:
        logging.info('Rain within ' + str(minutes) + ' minutes')
    else:
        logging.info('No rain in next hour'
                     )
    if state.notify_rain(minutes):
        logging.warning('Notification: Rain within ' + str(minutes) + ' minutes')
        sendmail.send_mail('Pluie dans ' + str(minutes) + ' minutes', "A l'abri !!!")


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)s %(filename)s:%(lineno)d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG,
                        stream=stdout)
    # logging.info('Minutes avant la pluie : ' + str(minutes_to_rain()))

    sched = scheduler.Scheduler(delay=60*5, callback=loop)
    sched.start()
