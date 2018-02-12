PH = '?'  # placeholder


def _rail(rails):
    cur, inc = 0, -1
    yield cur
    while True:
        if cur + 1 == rails or cur == 0:
            inc = -inc
        cur += inc
        yield cur


def encode(message, rails):
    board = [[None]*len(message) for i in range(rails)]
    for i, j, c in zip(_rail(rails), range(len(message)), message):
        board[i][j] = c

    result = []
    for row in board:
        result.extend([x for x in row if x is not None])

    return ''.join(result)


def decode(encoded_message, rails):
    board = [[None] * len(encoded_message) for i in range(rails)]
    for i, j, c in zip(_rail(rails), range(len(encoded_message)), encoded_message):
        board[i][j] = PH

    message = list(reversed(encoded_message))
    for row in board:
        for i in range(len(row)):
            if row[i] == PH:
                row[i] = message.pop()

    result = []
    for i, j in zip(_rail(rails), range(len(encoded_message))):
        result.append(board[i][j])
    return ''.join(result)
