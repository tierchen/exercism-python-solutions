class Garden(object):
    kids_default = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                    'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    plants_mapping = {'C': 'Clover',
                      'G': 'Grass',
                      'V': 'Violets',
                      'R': 'Radishes'}

    def __init__(self, diagram, students=kids_default):
        self.possession = {}
        row1, row2 = diagram.split()
        for i, student in enumerate(students):
            try:
                self.possession[student] = [row1[2*i], row1[2*i+1], row2[2*i], row2[2*i+1]]
            except IndexError:
                break

    def plants(self, student):
        return list(map(lambda x: self.plants_mapping[x], self.possession[student]))


