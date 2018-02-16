from collections import namedtuple
_Move = namedtuple('Move', ['x', 'y'])
_moves = [_Move(x, y) for x, y in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]]


def is_legit_characters(b):
    return set(''.join(b)) <= set('* ')


def is_matrix(b):
    return len({len(row) for row in b}) < 2


def increment(b, x, y):
    for move in _moves:
        if 0 <= x + move.x < len(b) and 0 <= y + move.y < len(b[0]) and b[x + move.x][y + move.y] != '*':
            b[x + move.x][y + move.y] += 1


def board(input_board_array):
    if not is_legit_characters(input_board_array):
        raise ValueError('Invalid input character')
    if not is_matrix(input_board_array):
        raise ValueError('Not a matrix')

    b = [[0 if x == ' ' else '*' for x in row] for row in input_board_array]
    for i, row in enumerate(b):
        for j, x in enumerate(row):
            if x == '*':
                increment(b, i, j)
    return [''.join(map(lambda x: ' ' if x == 0 else str(x), row)) for row in b]
