from itertools import chain


def append(xs, ys):
    return [x for x in chain(xs, ys)]


def concat(lists):
    return [x for x in chain.from_iterable(lists)]


def filter_clone(function, xs):
    return [x for x in xs if function(x)]


def length(xs):
    cnt = 0
    for _ in xs:
        cnt += 1
    return cnt


def map_clone(function, xs):
    return [function(x) for x in xs]


def foldl(function, xs, acc):
    for x in xs:
        acc = function(acc, x)
    return acc


def foldr(function, xs, acc):
    for x in xs[::-1]:
        acc = function(x, acc)
    return acc


def reverse(xs):
    return xs[::-1]
