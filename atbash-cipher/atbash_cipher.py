import string


def prepare(text):
    return ''.join([c for c in text.lower() if c in set(string.ascii_lowercase + string.digits)])


def group(text, n):
    return ' '.join([text[i:i+n] for i in range(0, len(text), n)])


def encode(plain_text):
    table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    result = prepare(plain_text).translate(table)
    return group(result, 5)


def decode(ciphered_text):
    table = str.maketrans(string.ascii_lowercase[::-1], string.ascii_lowercase)
    return prepare(ciphered_text).translate(table)
