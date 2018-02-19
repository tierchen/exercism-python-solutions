NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs=None):
        self.name = name
        self.attrs = {}
        if attrs is not None:
            self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs=None):
        self.src = src
        self.dst = dst
        self.attrs = {}
        if attrs is not None:
            self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        data = data or []

        if any(len(item) < 2 for item in data):
            raise TypeError('malformed graph or item')

        if any(len(params) != 2 for t, *params in data if t in [NODE, ATTR]) \
                or any(len(params) != 3 for t, *params in data if t == EDGE):
            raise ValueError('malformed item')

        if {t for t, *_ in data} - {NODE, EDGE, ATTR}:
            raise ValueError('unknown item')

        self.nodes = [Node(*params) for t, *params in data if t == NODE]
        self.edges = [Edge(*params) for t, *params in data if t == EDGE]
        self.attrs = {attr: value for t, *params in data if t == ATTR for attr, value in [params]}
