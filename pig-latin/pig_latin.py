import re

vowels_patterns = [r'^(xr)',
                   r'[^q](u)', r'^(u)',
                   r'[^eioa](y)', r'(y)[^eioa]',
                   r'([eioa])']


def first_vowel(word):
    result = []
    for pattern in vowels_patterns:
        s = re.search(pattern, word)
        if s is not None:
            result.append(s.start(1))
    return min(result) if result else len(word)


def translate(text):
    result = []
    for word in text.split():
        fv = first_vowel(word)
        result.append(word[fv:] + word[:fv] + 'ay')
    return ' '.join(result)
