SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(first_list, second_list):
    first = '-'.join(map(str, first_list))
    second = '-'.join(map(str, second_list))
    if first == second:
        return EQUAL
    elif first in second:
        return SUBLIST
    elif second in first:
        return SUPERLIST
    else:
        return UNEQUAL
