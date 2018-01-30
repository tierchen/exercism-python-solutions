import re


def decode(string):
    matches = re.finditer(r'([\d]*)([a-zA-Z\s])', string)
    print(list(matches)[0])
    return ''.join(int(match or '1')*ch for match, ch in matches)


def encode(string):
    matches = re.findall(r'(([a-zA-Z\s])\2*)', string)
    return ''.join([str('' if len(match) == 1 else len(match)) + ch for match, ch in matches])
