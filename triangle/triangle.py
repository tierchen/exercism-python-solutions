def is_valid_triangle(func):
    def wrapper(sides):
        *remain, c = sorted(sides)
        return sum(remain) > c and min(remain) > 0 and func(sides)
    return wrapper


@is_valid_triangle
def is_equilateral(sides):
    return len(set(sides)) == 1


@is_valid_triangle
def is_isosceles(sides):
    return len(set(sides)) <= 2


@is_valid_triangle
def is_scalene(sides):
    return not is_isosceles(sides)
