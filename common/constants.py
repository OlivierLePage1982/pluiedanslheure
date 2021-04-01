import os

# Environment variables
RAIN_TOKEN = os.environ.get('RAIN_TOKEN', default='')
PUSH_TOKEN = os.environ.get('PUSHBULLET_TOKEN', default='')
SMTP_USERNAME = os.environ.get('SMTP_USERNAME', default='')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', default='')

# Global constants
DEBUG = True
RAIN_URL = 'https://rpcache-aa.meteofrance.com/internet2018client/2.0/nowcast/' \
           'rain?lat={lat}&lon={lon}&token=' + RAIN_TOKEN
DEFAULT_LAT = 48.596866
DEFAULT_LON = -1.252042
PUSH_URL = 'https://api.pushbullet.com/v2/pushes'

