import re
import operator as op

OPERATIONS_MAPPING = {
    'plus': op.add,
    'minus': op.sub,
    'multiplied by': op.mul,
    'divided by': op.floordiv,
}


def calculate(question):
    match = re.match(r'What is (-?\d+) ((?:(?:{}) (?:-?\d+)\s?)+)\?$'.format('|'.join(OPERATIONS_MAPPING)), question)
    if not match:
        raise ValueError('Invalid input (pattern: \'What is {num} [{operation} by {num}]+?)\'')
    a, following = int(match.group(1)), match.group(2)
    operations = [(OPERATIONS_MAPPING[m.group(1)], int(m.group(2)))
                  for m in re.finditer(r'({}) (-?\d+)\s?'.format('|'.join(OPERATIONS_MAPPING)), following)][::-1]
    while operations:
        o, b = operations.pop()
        a = o(a, b)
    return a
