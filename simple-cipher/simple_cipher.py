from itertools import cycle
import random
import string

ENCODE, DECODE = range(2)


class Cipher(object):
    def __init__(self, key=None):
        if key is None:
            key = ''.join(random.choices(string.ascii_lowercase, k=random.randrange(100, 150)))
        elif not (key.isalpha() and key.islower()):
            raise ValueError('A random key must consist of lowercase letters only')
        self.key = key

    def _shift(self, text, code=ENCODE):
        result = []
        for letter, shift_letter in zip((ch.lower() for ch in text if ch.isalpha()), cycle(self.key)):
            shift = (-1)**code*(ord(shift_letter) - ord('a'))
            result.append(chr((ord(letter) + shift - ord('a')) % 26 + ord('a')))

        return ''.join(result)

    def encode(self, text):
        return self._shift(text, code=ENCODE)

    def decode(self, text):
        return self._shift(text, code=DECODE)


class Caesar(Cipher):
    def __init__(self):
        super().__init__('d')
