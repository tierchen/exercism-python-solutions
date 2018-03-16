class Clock(object):
    def __init__(self, hour, minute):
        delta_hour, self.minute = divmod(minute, 60)
        self.hour = (hour + delta_hour) % 24

    def __repr__(self):
        return '{:02}:{:02}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
