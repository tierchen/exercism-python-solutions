numbers = [''] + 'first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth'.split()
stuff = ['a Partridge in a Pear Tree',
         'two Turtle Doves',
         'three French Hens',
         'four Calling Birds',
         'five Gold Rings',
         'six Geese-a-Laying',
         'seven Swans-a-Swimming',
         'eight Maids-a-Milking',
         'nine Ladies Dancing',
         'ten Lords-a-Leaping',
         'eleven Pipers Piping',
         'twelve Drummers Drumming',
         ]


def verse(day_number):
    return 'On the {} day of Christmas my true love gave to me, {}.\n'.format(
        numbers[day_number],
        ', '.join(stuff[day_number-1:0:-1]) + (', and ' if day_number > 1 else '') + stuff[0]
    )


def verses(start, end):
    return '\n'.join([verse(i) for i in range(start, end+1)]) + '\n'


def sing():
    return verses(1, 12)
