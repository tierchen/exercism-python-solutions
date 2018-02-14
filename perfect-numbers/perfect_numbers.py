import operator as op
from itertools import combinations
from functools import reduce


def prime_factors(n):
    primes = []
    while n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                primes.append(i)
                n //= i
                break
        else:
            primes.append(n)
            break
    return primes


def factors(n):
    """All factors of the number n excluding n"""
    combs = []
    primes = prime_factors(n)
    for i in range(1, len(primes)):
        combs.extend(list(combinations(primes, i)))
    result = [1, ]
    for ms in combs:
        result.append(reduce(op.mul, ms))
    return list(set(result) - {n})


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
