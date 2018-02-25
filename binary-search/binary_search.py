def binary_search(list_of_numbers, number):
    i, j = 0, len(list_of_numbers)
    while i < j:
        m = (i + j) // 2
        if list_of_numbers[m] == number:
            return m
        elif list_of_numbers[m] < number:
            i = m + 1
        else:
            j = m
    raise ValueError('{} is not in list'.format(number))
