chess_board = [2**x for x in range(65)]


def check_range(x):
    if not 1 <= x <= 64:
        raise ValueError('11')


def on_square(integer_number):
    check_range(integer_number)
    return chess_board[integer_number-1]


def total_after(integer_number):
    check_range(integer_number)
    return sum(chess_board[:integer_number])
