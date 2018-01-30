class Allergies(object):
    allergies = ['eggs',
                 'peanuts',
                 'shellfish',
                 'strawberries',
                 'tomatoes',
                 'chocolate',
                 'pollen',
                 'cats']
    allergies_mapping = {x: 2**i for i, x in enumerate(allergies)}

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return bool(self.allergies_mapping[item] & self.score)

    @property
    def lst(self):
        return [alr for alr in self.allergies if self.is_allergic_to(alr)]