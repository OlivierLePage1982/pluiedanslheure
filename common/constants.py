import os

debug = True
rain_token = os.environ['RAIN_TOKEN']
rain_url = 'https://rpcache-aa.meteofrance.com/internet2018client/2.0/nowcast/' \
           'rain?lat={lat}&lon={lon}&token=' + rain_token
default_lat = 48.571926
default_lon = -1.259789
push_url = 'https://api.pushbullet.com/v2/pushes'
push_token = os.environ['PUSHBULLET_TOKEN']

if debug:
    print('PUSHBULLET: ' + push_token)
    print('RAIN' + rain_token)
