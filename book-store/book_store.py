import math
from itertools import combinations, chain


COST = 800
DISCOUNTS = [0, 0.05, 0.1, 0.2, 0.25]


def price(different_books):
    return COST * (1 - DISCOUNTS[len(different_books)-1]) * len(different_books)


def calculate_total(books, current_price=0, calculated=None):
    if calculated is None:
        calculated = {tuple(): 0}
    if tuple(sorted(books)) in calculated:
        return calculated[tuple(sorted(books))] + current_price

    present = set(books)
    result = math.inf
    for to_rem in chain.from_iterable(combinations(present, i) for i in range(1, len(present)+1)):
        rest = books[:]
        for r in to_rem:
            rest.remove(r)
        rest_total = calculate_total(rest, current_price + price(to_rem), calculated)
        calculated[tuple(sorted(rest))] = rest_total - (current_price + price(to_rem))
        result = min(result, rest_total)

    return result
