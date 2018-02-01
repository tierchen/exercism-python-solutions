import string


def is_pangram(sentence):
    sentence = ''.join([x for x in sentence.lower() if x.isalpha()])
    return len(set(sentence)) == len(string.ascii_lowercase)