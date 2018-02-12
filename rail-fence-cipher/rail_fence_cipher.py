from itertools import cycle, chain


def fence_pattern(message_size, rails):
    board = [[None]*message_size for _ in range(rails)]
    indexes = cycle(chain(range(0, rails-1), range(rails-1, 0, -1)))
    for i, j in zip(indexes, range(message_size)):
        board[i][j] = j
    return [x for row in board for x in row if x is not None]


def encode(message, rails):
    return ''.join([message[i] for i in fence_pattern(len(message), rails)])


def decode(encoded_message, rails):
    indexes = fence_pattern(len(encoded_message), rails)
    inverse_indexes = [None]*len(encoded_message)
    for i, j in enumerate(indexes):
        inverse_indexes[j] = i
    return ''.join([encoded_message[i] for i in inverse_indexes])
