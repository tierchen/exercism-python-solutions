from collections import Counter
import re


def word_count(phrase):
    phrase = re.sub(r'\'*[ !+@#$%^&*(){}\[\]:;,._]+\'*', ' ', phrase.lower())
    return dict(Counter(phrase.split()))