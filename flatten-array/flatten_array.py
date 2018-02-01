def flatten_gen(iterable):
    for x in iterable:
        if isinstance(x, (tuple, list)):
            yield from flatten_gen(x)
        else:
            yield x


def flatten(iterable):
    return [x for x in flatten_gen(iterable) if x is not None]
