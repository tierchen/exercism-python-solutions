from string import ascii_uppercase


def make_diamond(letter):
    n = ascii_uppercase.index(letter)
    return ''.join([''.join([' '*i,
                             ascii_uppercase[n-i],
                             ' '*(-1 + (n-i)*2 + (1 if i==n else 0)),
                             ascii_uppercase[n-i]*(i!=n),
                             ' '*i,
                             '\n'])
                    for i in map(abs, range(n, -n-1, -1))])
