units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousands = ['', 'thousand', 'million', 'billion']


def clear_join(delimiter, iterable):
    return delimiter.join(list(filter(lambda x: x != '', iterable)))


def say_hundred(number):
    if number == 0:
        return ''
    elif number < 20:
        return (units + teens)[number]
    else:
        decade, unit = divmod(number, 10)
        return clear_join('-', [tens[decade], units[unit]])


def say_thousand(number, verbose=False):
    hundred, unit = divmod(number, 100)
    return clear_join(' ', [units[hundred], 'hundred'*bool(hundred),
                            'and'*bool((hundred or verbose) and unit), say_hundred(unit)])


def say(number):
    if number == 0:
        return 'zero'
    elif number < 0:
        raise ValueError('Can\'t spell out negative number')
    elif number >= 1000**len(thousands):
        raise ValueError('Can\'t spell out such a big number')

    result = []
    groups = list(map(int, '{:,}'.format(int(number)).split(',')[::-1]))
    for i, e, g in zip(range(len(thousands)), thousands, groups):
        result.append(clear_join(' ', [say_thousand(g,
                                                    verbose=bool(groups[i+1:] and i == 0)),  # if next group exists
                                       e*bool(g)]))
    return clear_join(' ', result[::-1])