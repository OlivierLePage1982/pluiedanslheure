import unittest


class RainNotificationStateMachine:

    def __init__(self):
        self.rain_in_progress = False

    def notify_rain(self, minutes_to_rain) -> bool:
        if not self.rain_in_progress and (0 <= minutes_to_rain <= 30):
            self.rain_in_progress = True
            return True
        elif minutes_to_rain == -1:
            self.rain_in_progress = False
            return False
        return False


class StateMachineTest(unittest.TestCase):

    def test_rain_twice(self):
        state = RainNotificationStateMachine()
        # First update, no rain => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Second update, rain in 20 mins => notification
        self.assertEqual(True, state.notify_rain(20))
        # Third update, rain in 10 mins => no notification
        self.assertEqual(False, state.notify_rain(10))
        # Fourth update, no rain next hour => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Fifth update, rain in 45 mins => no notification
        self.assertEqual(False, state.notify_rain(45))
        # Sixth update, rain in 15 mins => notification
        self.assertEqual(True, state.notify_rain(15))

    def test_rain_three_times(self):
        state = RainNotificationStateMachine()
        # First update, no rain => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Second update, rain in 20 mins => notification
        self.assertEqual(True, state.notify_rain(20))
        # Third update, rain in progress => no notification
        self.assertEqual(False, state.notify_rain(0))
        # Fourth update, rain in progress => no notification
        self.assertEqual(False, state.notify_rain(0))
        # Fifth update, rain in 45 mins => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Sixth update, rain in 15 mins => notification
        self.assertEqual(True, state.notify_rain(15))
        # Seventh update, rain in progress => no notification
        self.assertEqual(False, state.notify_rain(0))
        # Eighth update, no more rain => no notification
        self.assertEqual(False, state.notify_rain(-1))
        # Ninth update, rain again in 20 mins => notification
        self.assertEqual(True, state.notify_rain(20))
