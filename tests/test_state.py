import unittest
from forecast.state import RainNotificationStateMachine


class StateMachineTest(unittest.TestCase):

    def test_rain_twice(self):
        state = RainNotificationStateMachine()
        # First update, no rain => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Second update, rain in 20 mins => no notification, need confirmation
        self.assertEqual(False, state.notify_rain(20))
        # Third update, rain in 10 mins => notification
        self.assertEqual(True, state.notify_rain(10))
        # Fourth update, no rain next hour => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Fifth update, rain in 45 mins => no notification
        self.assertEqual(False, state.notify_rain(45))
        # Sixth update, rain in 15 mins => no notification, need confirmation
        self.assertEqual(False, state.notify_rain(15))
        # Seventh update, rain in 5 mins => notification
        self.assertEqual(False, state.notify_rain(15))

    def test_rain_three_times(self):
        state = RainNotificationStateMachine()
        # First update, no rain => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Second update, rain in 20 mins => no notification, need confirmation
        self.assertEqual(False, state.notify_rain(20))
        # Third update, rain in progress => notification
        self.assertEqual(True, state.notify_rain(0))
        # Fourth update, rain in progress => no notification
        self.assertEqual(False, state.notify_rain(0))
        # Fifth update, rain in 45 mins => no notification
        self.assertEqual(False, state.notify_rain(45))
        # Sixth update, rain in 15 mins => no notification, need confirmation
        self.assertEqual(False, state.notify_rain(15))
        # Seventh update, rain in 5 mins => notification
        self.assertEqual(True, state.notify_rain(5))
        # Eighth update, no more rain => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Ninth update, rain again in 20 mins => no notification
        self.assertEqual(False, state.notify_rain(20))
        # Tenth update, rain again in 10 mins => notification
        self.assertEqual(True, state.notify_rain(10))

    def test_rain_postponed(self):
        state = RainNotificationStateMachine()
        # First update, no rain => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Second update, rain in 10 mins => no notification, need confirmation
        self.assertEqual(False, state.notify_rain(10))
        # Third update, rain in 10 mins => no notification, still not confirmed
        self.assertEqual(False, state.notify_rain(10))
        # Fourth update, rain in 5 mins => notification
        self.assertEqual(True, state.notify_rain(5))

    def test_rain_bug(self):
        state = RainNotificationStateMachine()
        self.assertEqual(False, state.notify_rain(-1))
        self.assertEqual(False, state.notify_rain(32))
        self.assertEqual(False, state.notify_rain(27))
        self.assertEqual(True, state.notify_rain(22))
        self.assertEqual(False, state.notify_rain(17))
        self.assertEqual(False, state.notify_rain(12))
        self.assertEqual(False, state.notify_rain(7))
