OPEN = list('{([')
CLOSED = list('})]')
CLOSE_OPEN_MAPPING = {x: y for x, y in zip(CLOSED, OPEN)}


def check_brackets(input_string):
    brackets = []
    for ch in input_string:
        if ch in OPEN:
            brackets.append(ch)
        elif ch in CLOSED:
            if brackets and brackets[-1] == CLOSE_OPEN_MAPPING[ch]:
                brackets.pop()
            else:
                return False
    return not brackets
