from itertools import combinations


def is_rectangle(points, ascii_diagram):
    if len({point[0] for point in points}) == len({point[1] for point in points}) == 2:
        p1, p2, p3, p4 = sorted(points)
        if set(ascii_diagram[p1[0]][p1[1]+1:p2[1]]).union(set(ascii_diagram[p3[0]][p3[1]+1:p4[1]])) <= set('-+') \
                and set(''.join([row[p1[1]] + row[p2[1]] for row in ascii_diagram[p1[0]+1:p3[0]]])) <= set('|+'):
            return True
    return False


def count(ascii_diagram):
    points = [(i, j) for i, row in enumerate(ascii_diagram) for j, ch in enumerate(row) if ch == '+']
    cnt = 0
    for points in combinations(points, 4):
        if is_rectangle(points, ascii_diagram):
            cnt += 1
    return cnt
