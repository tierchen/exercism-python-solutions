from itertools import combinations_with_replacement
from collections import defaultdict


def palindrome_products(min_factor, max_factor, f):
    if min_factor > max_factor:
        raise ValueError('Max_factor should be greater than or equal to min_factor')
    prods = defaultdict(set)
    for a, b in combinations_with_replacement(range(min_factor, max_factor + 1), 2):
        prod = str(a*b)
        if prod == prod[::-1]:
            prods[a * b].add((a, b))
    if not prods:
        raise ValueError('Empty list of palindromes')
    result = f(prods)
    return result, prods[result]


def largest_palindrome(min_factor, max_factor):
    return palindrome_products(min_factor, max_factor, max)


def smallest_palindrome(min_factor, max_factor):
    return palindrome_products(min_factor, max_factor, min)
