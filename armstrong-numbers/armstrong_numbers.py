def is_armstrong(number):
    p = len(str(number))
    numbers = map(int, str(number))
    return sum(map(lambda n: pow(n, p), numbers)) == number
