"""
Barning, F. J. M. (1963),
"Over pythagorese en bijna-pythagorese driehoeken en een generatieproces met behulp van unimodulaire matrices"
"""

A = [[1, -2, 2],
     [2, -1, 2],
     [2, -2, 3]]

B = [[1, 2, 2],
     [2, 1, 2],
     [2, 2, 3]]

C = [[-1, 2, 2],
     [-2, 1, 2],
     [-2, 2, 3]]

FIRST_TRIPLET = [3, 4, 5]


def multiply(matrix1, vector2):
    return [sum([a*b for a, b in zip(vector1, vector2)]) for vector1 in matrix1]


def triplets_tree_level():
    new_triplets = (FIRST_TRIPLET, )
    while True:
        last_triplets = yield new_triplets
        new_triplets = [multiply(matrix, triplet) for triplet in last_triplets for matrix in (A, B, C)]


def primitive_triplets(number_in_triplet):
    if number_in_triplet % 4:  # although in my implementation any value is allowed
        raise ValueError('arg should be an integer divisible by 4')  # unnecessary checkup to pass last test
    result = []
    coroutine = triplets_tree_level()
    triplets = next(coroutine)
    while triplets:
        result.extend(filter(lambda triplet: number_in_triplet in triplet, triplets))
        triplets = coroutine.send(filter(lambda triplet: min(triplet) < number_in_triplet, triplets))

    return set(map(lambda vect: tuple(sorted(vect)), result))


def triplets_in_range(range_start, range_end):
    result = []
    coroutine = triplets_tree_level()
    triplets = next(coroutine)
    while triplets:
        for triplet in triplets:
            for k in range((range_start + 2)//min(triplet), range_end//max(triplet) + 1):
                if range_start <= k*min(triplet) <= k*max(triplet) <= range_end:
                    result.append(tuple(map(lambda x: k*x, triplet)))
        triplets = coroutine.send(filter(lambda triplet: min(triplet) <= range_end, triplets))

    return set(map(lambda vect: tuple(sorted(vect)), result))


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2

