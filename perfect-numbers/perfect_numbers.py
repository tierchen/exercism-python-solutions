from itertools import chain


def factors(n):
    """All factors of the number n excluding n"""
    return list(set(chain.from_iterable((i, n//i) for i in range(1, int(n**0.5) + 1) if n % i == 0)) - {n})


def classify(number):
    if number < 1:
        raise ValueError('The classifying number must be greater than 1')
    fs = sum(factors(number))
    if fs == number:
        return 'perfect'
    elif fs > number:
        return 'abundant'
    else:
        return 'deficient'
