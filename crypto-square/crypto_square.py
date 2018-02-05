import re
from math import sqrt, floor, ceil
from itertools import zip_longest
from string import punctuation


def encode(plain_text):
    text = re.sub(r'[\s{}]+'.format(punctuation), '', plain_text.lower())
    side = sqrt(len(text))
    c, r = ceil(side), floor(side)
    if c*r < len(text):
        r += 1

    return ' '.join([''.join([' ' if x is None else x for x in row])
            for row in zip_longest(*[text[c*i:c*(i+1)] for i in range(r)])])
