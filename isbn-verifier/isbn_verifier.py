def verify(isbn):
    if not isbn or not set(isbn[:-1]) <= set('1234567890-') or isbn[-1] not in '1234567890X':
        return False
    check = [int(x) for x in isbn[:-1] if x.isdigit()]
    if isbn[-1] == 'X':
        check.append(10)
    else:
        check.append(int(isbn[-1]))
    if sum([x*y for x, y in zip(check, range(10, 0, -1))]) % 11 == 0:
        return True
    else:
        return False