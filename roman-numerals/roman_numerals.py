roman = {
    0: '',
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}


def numeral(number):
    result = []
    orders = list(map(int, str(number)))
    for order, num in enumerate(orders[::-1]):
        result.append(fragmentation(num, order))
    return ''.join(result[::-1])


def fragmentation(number, order=0):
    if 2 <= number <= 3:
        return roman[1 * 10**order] * number
    elif number == 4:
        return roman[1 * 10**order] + roman[5 * 10**order]
    elif 6 <= number <= 8:
        return roman[5 * 10**order] + roman[1 * 10**order] * (number % 5)
    elif number == 9:
        return roman[1 * 10**order] + roman[1 * 10**(order + 1)]
    else:
        return roman[number * 10**order]