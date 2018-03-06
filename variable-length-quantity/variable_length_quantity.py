def encode(numbers):
    bytes_ = []
    for number in numbers:
        current = []
        byte = number & 0x7F
        current.append(byte)
        number >>= 7
        while number:
            current.append(0x80 | (number & 0x7F))
            number >>= 7
        bytes_.extend(reversed(current))
    return bytes_


def decode(bytes_):
    numbers, number = [], 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if not byte & 0x80:
            numbers.append(number)
            number = 0
    if number or not numbers:
        raise ValueError('Incomplete or wrong sequence')
    return numbers
