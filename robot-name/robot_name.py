import random
import string


class Robot:
    _previous_names = {None}

    def __init__(self, name=None):
        if name is None:
            while name in Robot._previous_names:
                name = self._random_name()

        Robot._previous_names.add(name)
        self.name = name

    @staticmethod
    def _random_name(ascii=2, digits=3):
        return ''.join([random.choice(string.ascii_uppercase) for i in range(ascii)] +
                       [random.choice(string.digits) for i in range(digits)])

    def reset(self):
        self.__init__()
