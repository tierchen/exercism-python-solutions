def _retrieve(grid):
    m, n = len(grid), len(list(zip(*grid)))
    if m % 4 or n % 3:
        raise ValueError('Invalid grid size')
    return [[tuple(grid[i][3*jj : 3*jj + 3] for i in range(4*ii, 4*ii + 4))
            for jj in range(n//3)]
            for ii in range(m//4)]


numbers = {x: i for i, x in zip(map(str, range(10)), _retrieve(
    [" _     _  _     _  _  _  _  _ ",
     "| |  | _| _||_||_ |_   ||_||_|",
     "|_|  ||_  _|  | _||_|  ||_| _|",
     "                              "])[0])}


def convert(input_grid):
    return ','.join([''.join([numbers.get(num, '?') for num in row]) for row in _retrieve(input_grid)])
