import re


class Phone(object):
    def __init__(self, phone_number):
        match = re.match(r'1?([2-9]\d{2}[2-9]\d{6})$', ''.join(filter(str.isdigit, phone_number)))
        if not match:
            raise ValueError('Invalid phone number')
        self.number = match.group(1)

    @property
    def area_code(self):
        return self.number[:3]

    @property
    def local_number(self):
        return self.number[3:]

    def pretty(self):
        return ''.join(['(', self.area_code, ') ', self.local_number[:3], '-', self.local_number[3:]])
