from itertools import count


def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError("There is no {}th prime".format(positive_number))
    primes = [2]
    while len(primes) != positive_number:
        for cur in count(primes[-1]+1):
            for prime in primes:
                if cur % prime == 0:
                    break
            else:
                primes.append(cur)
                break
    return primes[-1]
