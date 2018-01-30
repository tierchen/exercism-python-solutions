from functools import reduce
import operator as op


def largest_product(series, size):
    if size > len(series):
        raise ValueError('Can\'t retrieve any series of this size')
    if size < 0:
        raise ValueError('Size can\'t be negative')
    series = list(map(int, series))
    result = 0
    for i in range(len(series)-size+1):
        cut_product = reduce(op.mul, series[i:i+size], 1)
        result = max(cut_product, result)
    return result
