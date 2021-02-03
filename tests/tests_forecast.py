import unittest
from forecast.rain import is_raining_next_hour_json
from forecast.rain import is_raining_next_hour
from forecast.rain import minutes_to_rain_json
from forecast.rain import minutes_to_rain
import json
import datetime


class ForecastTest(unittest.TestCase):

    def test_no_rain(self):
        with open('test_will_not_rain.json', 'r') as file:
            self.assertEqual(is_raining_next_hour_json(json.loads(file.read())), False)

    def test_will_rain(self):
        with open('test_will_rain.json', 'r') as file:
            self.assertEqual(is_raining_next_hour_json(json.loads(file.read())), True)

    def test_cover_get(self):
        is_raining_next_hour(lat=48.571926, lon=-1.259789)
        self.assertIn(minutes_to_rain(lat=48.571926, lon=-1.259789), range(-1, 60))

    def test_will_rain_minutes(self):
        with open('test_will_rain.json', 'r') as file:
            content = json.loads(file.read())
            update_time = datetime.datetime.strptime(content["update_time"], '%Y-%m-%dT%H:%M:%S.%fZ')
            self.assertEqual(minutes_to_rain_json(content, update_time), 25)

    def test_will_not_rain_minutes(self):
        with open('test_will_not_rain.json', 'r') as file:
            content = json.loads(file.read())
            update_time = datetime.datetime.strptime(content["update_time"], '%Y-%m-%dT%H:%M:%S.%fZ')
            self.assertEqual(minutes_to_rain_json(content, update_time), -1)
