from itertools import zip_longest


def transpose(input_lines):
    return '\n'.join(''.join(col).rstrip('-').replace('-', ' ')
                     for col in zip_longest(*input_lines.splitlines(), fillvalue='-'))
