import forecast.state
from forecast.rain import minutes_to_rain
import logging
from sys import stdout
from common import scheduler
from common import sendmail
from common import sendpush
from forecast import state


state = forecast.state.RainNotificationStateMachine()


def loop():
    minutes = minutes_to_rain()
    if minutes >= 0:
        logging.info('Rain within ' + str(minutes) + ' minutes')
    else:
        logging.info('No rain in next hour')
    if state.notify_rain(minutes):
        logging.warning('Notification: Rain within ' + str(minutes) + ' minutes')
        for notify in [sendmail.send_mail, sendpush.send_push]:
            notify('Pluie dans ' + str(minutes) + ' minutes', 'A l\'abri !!!')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)s %(filename)s:%(lineno)d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG,
                        stream=stdout)

    sched = scheduler.Scheduler(delay=60*5, callback=loop)
    sched.start()
