import unittest
from forecast.rain import minutes_to_rain_json
import json
import datetime


class ForecastTest(unittest.TestCase):

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

    def test_invalid_json(self):
        invalid_json = json.loads('{ "bad": "value"}')
        self.assertEqual(minutes_to_rain_json(invalid_json, datetime.datetime.now()), -1)
