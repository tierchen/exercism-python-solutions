subjects = [
    'house that Jack built', 'malt', 'rat', 'cat', 'dog', 'cow with the crumpled horn', 'maiden all forlorn',
    'man all tattered and torn', 'priest all shaven and shorn', 'rooster that crowed in the morn',
    'farmer sowing his corn', 'horse and the hound and the horn',
]

actions = [
    'lay in', 'ate', 'killed', 'worried', 'tossed', 'milked', 'kissed', 'married', 'woke', 'kept', 'belonged to'
]


def verse(verse_num):
    return '\n'.join(
        ['This is the ' + subjects[verse_num]]
        + [' '.join(['that', ac, 'the', an]) for ac, an in zip(
            actions[:verse_num][::-1],
            subjects[:verse_num][::-1])]
    ) + '.'


def rhyme():
    return '\n\n'.join([verse(i) for i in range(len(subjects))])
