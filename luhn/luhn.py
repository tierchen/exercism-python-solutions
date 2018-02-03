import re


class Luhn(object):
    def __init__(self, card_num):
        card_num_cleaned = re.sub(r'\s+', '', card_num)
        self.card_num = card_num_cleaned

    def is_valid(self):
        if self.card_num.isdigit():
            cn = list(map(int, self.card_num))
            if len(cn) > 1 and sum([x * 2 - 9 if x * 2 > 9 else x * 2 for x in cn[-2::-2]] + cn[::-2]) % 10 == 0:
                return True
        return False
