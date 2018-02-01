import re


class SpaceAge(object):
    yoe = 31557600

    year_on_ = {
        'Mercury': 0.2408467 * yoe,
        'Venus': 0.61519726 * yoe,
        'Earth': 1 * yoe,
        'Mars': 1.8808158 * yoe,
        'Jupiter': 11.862615 * yoe,
        'Saturn': 29.447498 * yoe,
        'Uranus': 84.016846 * yoe,
        'Neptune': 164.79132 * yoe,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def __getattr__(self, item):
        match = re.match(r'on_(?P<planet>\w+)', item)
        if match:
            planet = match.group('planet').title()
            if planet in self.year_on_:
                return lambda: round(self.seconds / self.year_on_[planet], 2)
            else:
                raise AttributeError('There is no such (known) planet')

    def qwe(self):
        return 1

print(SpaceAge(10).qwe())