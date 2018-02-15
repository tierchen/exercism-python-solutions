def _palindrome(min_factor, max_factor, op):
    xs = [(x*y, (x, y))
          for x in range(min_factor, max_factor+1)
          for y in range(x, max_factor+1)
          for s in [str(x*y)]
          if s == s[::-1]]
    a, b = op(xs)
    return a, {q for p, q in xs if p == a}


def largest_palindrome(min_factor, max_factor):
    return  _palindrome(min_factor, max_factor, max)


def smallest_palindrome(min_factor, max_factor):
    return _palindrome(min_factor,max_factor, min)


import timeit
print(timeit.timeit('largest_palindrome(min_factor=1000, max_factor=9999)', 'from __main__ import largest_palindrome', number=1))