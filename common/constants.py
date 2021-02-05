import os

# Environment variables
RAIN_TOKEN = os.environ['RAIN_TOKEN']
PUSH_TOKEN = os.environ['PUSHBULLET_TOKEN']
SMTP_USERNAME = os.environ['SMTP_USERNAME']
SMTP_PASSWORD = os.environ['SMTP_PASSWORD']

# Global constants
DEBUG = True
RAIN_URL = 'https://rpcache-aa.meteofrance.com/internet2018client/2.0/nowcast/' \
           'rain?lat={lat}&lon={lon}&token=' + RAIN_TOKEN
DEFAULT_LAT = 48.571926
DEFAULT_LON = -1.259789
PUSH_URL = 'https://api.pushbullet.com/v2/pushes'

if DEBUG:
    print('PUSHBULLET: ' + PUSH_TOKEN)
    print('RAIN: ' + RAIN_TOKEN)
