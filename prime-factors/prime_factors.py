def prime_factors(natural_number):
    result = []
    i = 2
    while i**2 <= natural_number:
        if natural_number % i == 0:
            result.append(i)
            natural_number //= i
        else:
            i += 1
    if natural_number != 1:
        result.append(natural_number)
    return result
