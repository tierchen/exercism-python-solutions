def sum_of_multiples(limit, multiples):
    result = []
    for m in multiples:
        result.extend(list(range(m, limit, m)))
    return sum(set(result))
