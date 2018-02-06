import re
from math import sqrt, ceil
from itertools import zip_longest
from string import punctuation


def encode(plain_text):
    text = re.sub(r'[\s{}]+'.format(punctuation), '', plain_text.lower())

    c = ceil(sqrt(len(text)))
    if c == 0:
        return ''

    text_sliced = [text[i:i+c] for i in range(0, len(text), c)]

    return ' '.join([''.join(row) for row in zip_longest(*text_sliced, fillvalue=' ')])
