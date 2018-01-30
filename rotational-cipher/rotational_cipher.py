def rotate(text, key):
    result = []
    for ch in text:
        if ch.isalpha():
            shift = 97 if ch.islower() else 65
            result.append(chr((ord(ch) - shift + key) % 26 + shift))
        else:
            result.append(ch)
    return ''.join(result)