codes = 'wink!double blink!close your eyes!jump'.split('!')


def handshake(number):
    actions = [x for i, x in enumerate(codes) if number & (1 << i)]
    return actions[::-1] if number & 16 else actions


def secret_code(actions):
    number = sum([1 << codes.index(action) for action in actions])
    return number + 16*(len(actions) > 1 and handshake(number)[::-1] == actions)
