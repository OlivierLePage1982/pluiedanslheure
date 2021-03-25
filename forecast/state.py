class RainNotificationStateMachine:

    def __init__(self):
        self.rain_detected = False
        self.last_mins_to_rain = -1
        self.rain_confirmed = False

    def notify_rain(self, minutes_to_rain) -> bool:
        if minutes_to_rain == -1 or minutes_to_rain > 30:
            self.rain_detected = False
            self.rain_confirmed = False
            self.last_mins_to_rain = -1
            return False
        elif 0 <= minutes_to_rain <= 30:
            if not self.rain_detected:
                self.rain_detected = True
                self.last_mins_to_rain = minutes_to_rain
                return False
            elif minutes_to_rain < self.last_mins_to_rain and not self.rain_confirmed:
                self.rain_confirmed = True
                self.last_mins_to_rain = minutes_to_rain
                return True
            else:
                self.last_mins_to_rain = minutes_to_rain
                return False
        return False
