from collections import defaultdict


class School(object):
    def __init__(self, name):
        self.name = name
        self.data = defaultdict(list)

    def add(self, student, grade):
        self.data[grade].append(student)

    def grade(self, grade):
        return self.data[grade]

    def sort(self):
        return [(grade, tuple(sorted(roster))) for grade, roster in sorted(self.data.items(), key=lambda x: x[0])]
