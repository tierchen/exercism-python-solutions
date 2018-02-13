def _matrix_fs(matrix, f):
    result = []
    for i, row in enumerate(matrix):
        sign = f(row)
        result.extend([(i, j) for j, x in enumerate(row) if x == sign])
    return result


def saddle_points(matrix):
    n, m = len(matrix), {len(row) for row in matrix}
    if n == 0:
        return set()
    if len(m) > 1:
        raise ValueError('The list of lists isn\'t a square matrix')
    m = m.pop()

    transposed_matrix = list(zip(*matrix))
    maximums, minimums = _matrix_fs(matrix, max), [(j, i) for i, j in _matrix_fs(transposed_matrix, min)]

    return set(maximums).intersection(set(minimums))
