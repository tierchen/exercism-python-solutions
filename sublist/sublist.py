SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(first_list, second_list):
    def is_sub(sub_list, super_list):
        if not sub_list:
            return True
        for i in range(len(super_list) - len(sub_list) + 1):
            if sub_list[0] == super_list[i] and sub_list == super_list[i:i+len(sub_list)]:
                return True
        return False

    if first_list == second_list:
        return EQUAL
    elif is_sub(first_list, second_list):
        return SUBLIST
    elif is_sub(second_list, first_list):
        return SUPERLIST
    else:
        return UNEQUAL
