def rebase(input_base, digits, output_base):
    if min(input_base, output_base) < 2:
        raise ValueError('Input/output bases should be >1')
    if not digits:
        return []
    if min(digits) < 0 or max(digits) >= input_base:
        raise ValueError('Wrong format')

    base10 = sum([digit*input_base**power for power, digit in enumerate(digits[::-1])])
    result = []
    while base10:
        base10, remain = divmod(base10, output_base)
        result.append(remain)
    return result[::-1]
