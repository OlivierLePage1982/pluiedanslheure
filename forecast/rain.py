import requests
import common.constants
from datetime import datetime
import logging


def is_raining_next_hour_json(content) -> bool:
    rain = False
    for timeslot in content["properties"]["forecast"]:
        if int(timeslot['rain_intensity']) > 1:
            rain = True
            if common.constants.debug:
                logging.debug(timeslot['time'] + ": " + str(timeslot['rain_intensity']))
    if common.constants.debug:
        logging.debug('No rain!' if not rain else 'It will rain next hour')
    return rain


def minutes_to_rain_json(content, update_time=datetime.now()) -> int:
    logging.info('Current date: ' + str(update_time))
    for timeslot in content["properties"]["forecast"]:
        if int(timeslot['rain_intensity']) > 1:
            rain_time = datetime.strptime(timeslot["time"], '%Y-%m-%dT%H:%M:%S.%fZ')
            logging.info('Rain date: ' + str(rain_time))
            minutes = int(rain_time.timestamp() - update_time.timestamp())//60
            if common.constants.debug:
                logging.debug('Rain in ' + str(minutes) + ' minutes' if minutes > 0 else 'No rain in next 60 minutes')
            return minutes
    return -1


def is_raining_next_hour(lat=common.constants.default_lat, lon=common.constants.default_lon) -> bool:
    url = common.constants.rain_url.format(lat=lat, lon=lon)
    if common.constants.debug:
        logging.debug(url)
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        return is_raining_next_hour_json(response.json())
    else:
        raise Exception('Response error code: ' + str(response.status_code))


def minutes_to_rain(lat=common.constants.default_lat, lon=common.constants.default_lon) -> int:
    url = common.constants.rain_url.format(lat=lat, lon=lon)
    if common.constants.debug:
        logging.debug(url)
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        return minutes_to_rain_json(response.json())
    else:
        raise Exception('Response error code: ' + str(response.status_code))