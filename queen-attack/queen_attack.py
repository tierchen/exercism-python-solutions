from itertools import chain


def check_valid_position(white_position, black_position):
    if white_position == black_position or not all(0 <= x < 8 for x in chain(white_position, black_position)):
        raise ValueError('Invalid queen position')


def board(white_position, black_position):
    check_valid_position(white_position, black_position)
    return [''.join(['W' if (x, y) == white_position else
                     'B' if (x, y) == black_position else
                     '_' for y in range(8)])
            for x in range(8)]


def can_attack(white_position, black_position):
    check_valid_position(white_position, black_position)
    x1, y1 = white_position
    x2, y2 = black_position
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
