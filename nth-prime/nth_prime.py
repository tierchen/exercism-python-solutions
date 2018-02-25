from itertools import count


def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError("There is no {}th prime".format(positive_number))
    primes = [2]

    for cur in count(primes[-1]+1):
        if len(primes) == positive_number:
            return primes[-1]
        stop = int(cur ** 0.5) + 1
        for prime in primes:
            if cur % prime == 0:
                break
            if prime >= stop:
                primes.append(cur)
                break
