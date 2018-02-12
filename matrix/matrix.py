class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [list(map(int, row.split())) for row in matrix_string.split('\n')]
        self._transposed_matrix = [list(column) for column in zip(*self._matrix)]

    @property
    def rows(self):
        return self._matrix

    @property
    def columns(self):
        return self._transposed_matrix

print(Matrix("1 4 9\n16 25 36").rows)