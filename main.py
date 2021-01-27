from forecast.rain import minutes_to_rain
import logging
from sys import stdout

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)s %(filename)s:%(lineno)d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO,
                        stream=stdout)
    logging.info('Minutes avant la pluie : ' + str(minutes_to_rain()))
