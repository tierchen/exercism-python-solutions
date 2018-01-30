def sieve(limit):
    operating = list(range(2, limit+1))
    result = []
    while operating:
        cur = operating.pop(0)
        result.append(cur)
        operating = list(filter(lambda x: x % cur, operating))

    return result
